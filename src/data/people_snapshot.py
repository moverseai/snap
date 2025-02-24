import logging
import os
import typing
from pathlib import Path

import cv2
import numpy as np
import roma
import torch
import trimesh
from PIL import Image

from src.data.subdivided_smpl import (_create_projection_matrices,
                                      _load_body_data, _rodrigues, _skinning,
                                      _subdivide, _traverse_kinematic_chain)

__all__ = ["PeopleSnapshot"]


log = logging.getLogger(__name__)


class PeopleSnapshot(torch.utils.data.Dataset):
    _SPLITS_ = {
        "male-4-casual": {
            "train": (0, 659, 6),
            "val": (660, 660, 6),
            "test": (660, 872, 6),
            "gender": "male",
        },
        "male-3-casual": {
            "train": (0, 455, 4),
            "val": (456, 456, 4),
            "test": (456, 675, 4),
            "gender": "male",
        },
        "female-4-casual": {
            "train": (0, 335, 4),
            "val": (335, 335, 4),
            "test": (335, 523, 4),
            "gender": "female",
        },
        "female-3-casual": {
            "train": (0, 445, 4),
            "val": (446, 446, 4),
            "test": (446, 647, 4),
            "gender": "female",
        },
    }

    def __init__(
        self,
        path: str,
        subject: str,
        split: str,
        models_path: str,
        level: int = 1,
        batch: int = 2,
        offsets_path: typing.Optional[str] = None,
        downscale: int = 1,
    ) -> None:
        super().__init__()
        self.batch = batch
        self.downscale = downscale
        self.videos = []
        image_files = sorted((Path(path) / subject / "images").glob("image_????.png"))
        mask_files = sorted((Path(path) / subject / "masks").glob("mask_????.npy"))
        start, end, skip = PeopleSnapshot._SPLITS_[subject][split]
        gender = PeopleSnapshot._SPLITS_[subject]["gender"]
        self.image_files = image_files[start:end:skip]
        self.mask_files = mask_files[start:end:skip]
        self.num_frames = len(self.image_files)
        perm = np.random.permutation(self.num_frames).tolist()
        self.image_files = np.asarray(self.image_files, dtype=object)[perm]
        self.mask_files = np.asarray(self.mask_files, dtype=object)[perm]
        body_data_path = os.path.join(
            models_path, "models", f"basicmodel_{gender[0]}_lbs_10_207_0_v1.1.0.pkl"
        )
        blendshapes, regressor, parents, template, faces, weights = _load_body_data(
            body_data_path
        )
        data = np.load(Path(path) / subject / "poses" / f"anim_nerf_{split}.npz")
        self.betas = data["betas"].squeeze()
        offsets = np.einsum(
            "vcb,b->vc", blendshapes[..., : self.betas.shape[-1]], self.betas
        )
        shaped = template + offsets
        shaped_joints = np.einsum("jv,vc->jc", regressor, shaped)
        extra_offsets = None
        if offsets_path and os.path.exists(offsets_path):
            extra_offsets = np.load(offsets_path)["offsets"]
        features = np.concatenate([regressor.T, weights], axis=-1)
        V, F, N, A = _subdivide(
            shaped, faces, features, level=level, offsets=extra_offsets
        )
        J_regressor, skinning_weights = torch.split(A, shaped_joints.shape[0], dim=-1)
        self.joints = shaped_joints
        self.parents = parents
        self.weights = skinning_weights.numpy()
        self.vertices = V.numpy()
        self.faces = F.numpy()
        areas = trimesh.Trimesh(self.vertices, self.faces, process=False).area_faces
        areas = torch.from_numpy(areas).float()
        vareas = torch.zeros(self.vertices.shape[0])
        for c in range(F.shape[-1]):
            vareas.scatter_add_(0, F[..., c], areas)
        self.areas = vareas.numpy()
        self.normals = torch.nn.functional.normalize(N, dim=-1).numpy()
        self.transl = data["transl"][perm]
        self.global_orient = data["global_orient"][perm]
        self.pose = data["body_pose"].reshape(-1, 23, 3)[perm]
        self.pose = _rodrigues(
            np.concatenate([self.global_orient[:, np.newaxis], self.pose], axis=1)
        )
        camera = np.load(Path(path) / subject / "cameras.npz")
        self.intrinsics = camera["intrinsic"][np.newaxis].astype(np.float32)
        if self.downscale > 1:
            self.intrinsics[..., :2, :] /= self.downscale
        self.width = camera["width"] / self.downscale
        self.height = camera["height"] / self.downscale
        self.projection_matrices = _create_projection_matrices(
            self.intrinsics, self.width, self.height
        )
        self.extrinsics = camera["extrinsic"][np.newaxis].astype(np.float32)
        self.view_matrices = self.extrinsics.transpose(0, 2, 1).copy()  # row major
        self.viewprojection_matrices = (
            (self.projection_matrices @ self.extrinsics).transpose(0, 2, 1).copy()
        )
        self.camera_positions = np.linalg.inv(self.extrinsics)[:, :3, 3]

    def __len__(self) -> int:
        return int(self.num_frames / self.batch) - int(self.num_frames % self.batch)

    def __getitem__(self, index) -> typing.Any:
        (
            imgs,
            masks,
            times,
            bxfs,
            normals,
            vertices,
            blended_quaternions,
            poses,
            translations,
            orientations,
        ) = ([], [], [], [], [], [], [], [], [], [])
        for i in range(self.batch):
            frame = cv2.imread(str(self.image_files[index * self.batch + i]))
            mask = np.load(str(self.mask_files[index * self.batch + i]))
            if self.downscale > 1:
                frame = np.array(Image.fromarray(frame).resize((int(self.width), int(self.height))))
                mask = cv2.resize(
                    mask, None, fx=1./self.downscale, fy=1./self.downscale, interpolation=cv2.INTER_NEAREST
                )
            imgs.append(
                np.flip(frame, -1).transpose(2, 0, 1).astype(np.float32) / 255.0
            )
            masks.append(mask[np.newaxis].astype(np.float32))
            times.append(
                np.array((index * self.batch + i) / self.num_frames).astype(np.float32)
            )
            j, xf = _traverse_kinematic_chain(
                self.pose[index * self.batch + i], self.joints, self.parents
            )
            v, n, bxf = _skinning(self.weights, self.vertices, xf, self.normals)
            Q = roma.rotmat_to_unitquat(torch.from_numpy(xf[:, :3, :3])).numpy()
            wQ = np.sqrt(self.weights[..., np.newaxis]) * Q[np.newaxis]
            evals, evecs = np.linalg.eigh(np.einsum("bki,bkj->bij", wQ, wQ))
            blended_quats = np.roll(evecs[..., -1], 1, axis=-1)  # XYZW -> WXYZ
            vertices.append(v + self.transl[index * self.batch + i])
            normals.append(n.squeeze())
            bxfs.append(bxf)
            blended_quaternions.append(blended_quats)
            poses.append(self.pose[index * self.batch + i])
            translations.append(self.transl[index * self.batch + i])
            orientations.append(self.global_orient[index * self.batch + i])
        return {
            "shaped_joints": self.joints,
            "vertices": np.stack(vertices),
            "normals": np.stack(normals),
            "blended_transforms": np.stack(bxfs),
            "blended_rotations_quat": np.stack(blended_quaternions),
            "faces": self.faces,
            "shaped": self.vertices,
            "skinning_weights": self.weights,
            "extrinsics": np.broadcast_to(self.extrinsics, (self.batch, 4, 4)),
            "intrinsics": np.broadcast_to(self.intrinsics, (self.batch, 3, 3)),
            "betas": self.betas,
            "pose": np.stack(poses),
            "transl": np.stack(translations),
            "global_orient": np.stack(orientations),
            "color": np.stack(imgs),
            "time": np.stack(times),
            "mask": np.stack(masks),
            "camera_position": np.broadcast_to(self.camera_positions, (self.batch, 3)),
            "view_projection_matrix": np.broadcast_to(
                self.viewprojection_matrices, (self.batch, 4, 4)
            ),
            "view_matrix": np.broadcast_to(self.view_matrices, (self.batch, 4, 4)),
            "vertex_areas": self.areas,
        }

        # frame1 = cv2.imread(str(self.image_files[index * 2]))
        # frame2 = cv2.imread(str(self.image_files[index * 2 + 1]))
        # mask1 = np.load(str(self.mask_files[index * 2]))
        # mask2 = np.load(str(self.mask_files[index * 2 + 1]))
        # imgs.append(np.flip(frame1, -1).transpose(2, 0, 1).astype(np.float32) / 255.0)
        # imgs.append(np.flip(frame2, -1).transpose(2, 0, 1).astype(np.float32) / 255.0)
        # masks.append(mask1[np.newaxis].astype(np.float32))
        # masks.append(mask2[np.newaxis].astype(np.float32))
        # times.append(np.array((index * 2) / self.num_frames).astype(np.float32))
        # times.append(np.array((index * 2 + 1) / self.num_frames).astype(np.float32))
        # j1, xf1 = _traverse_kinematic_chain(
        #     self.pose[index * 2], self.joints, self.parents
        # )
        # v1, n1, bxf1 = _skinning(self.weights, self.vertices, xf1, self.normals)
        # Q1 = roma.rotmat_to_unitquat(torch.from_numpy(xf1[:, :3, :3])).numpy()
        # wQ1 = np.sqrt(self.weights[..., np.newaxis]) * Q1[np.newaxis]
        # evals1, evecs1 = np.linalg.eigh(np.einsum("bki,bkj->bij", wQ1, wQ1))
        # blended_quats1 = np.roll(evecs1[..., -1], 1, axis=-1)  # XYZW -> WXYZ
        # # blended_quats1 = evecs1[..., -1]
        # j2, xf2 = _traverse_kinematic_chain(
        #     self.pose[index * 2 + 1], self.joints, self.parents
        # )
        # v2, n2, bxf2 = _skinning(self.weights, self.vertices, xf2, self.normals)
        # Q2 = roma.rotmat_to_unitquat(torch.from_numpy(xf2[:, :3, :3])).numpy()
        # wQ2 = np.sqrt(self.weights[..., np.newaxis]) * Q2[np.newaxis]
        # evals2, evecs2 = np.linalg.eigh(np.einsum("bki,bkj->bij", wQ2, wQ2))
        # blended_quats2 = np.roll(evecs2[..., -1], 1, axis=-1)  # XYZW -> WXYZ
        # # blended_quats2 = evecs2[..., -1]
        # return {
        #     "shaped_joints": self.joints,
        #     "vertices": np.stack(
        #         (v1 + self.transl[index * 2], v2 + self.transl[index * 2 + 1])
        #     ),
        #     "normals": np.stack((n1.squeeze(), n2.squeeze())),
        #     "blended_transforms": np.stack((bxf1, bxf2)),
        #     "blended_rotations_quat": np.stack((blended_quats1, blended_quats2)),
        #     "faces": self.faces,
        #     "shaped": self.vertices,
        #     "skinning_weights": self.weights,
        #     "extrinsics": np.broadcast_to(self.extrinsics, (2, 4, 4)),
        #     "intrinsics": np.broadcast_to(self.intrinsics, (2, 3, 3)),
        #     "betas": self.betas,
        #     "pose": np.stack((self.pose[index * 2], self.pose[index * 2 + 1])),
        #     "transl": np.stack((self.transl[index * 2], self.transl[index * 2 + 1])),
        #     "global_orient": np.stack(
        #         (self.global_orient[index * 2], self.global_orient[index * 2 + 1])
        #     ),
        #     "color": np.stack(imgs),
        #     "time": np.stack(times),
        #     "mask": np.stack(masks),
        #     "camera_position": np.broadcast_to(self.camera_positions, (2, 3)),
        #     "view_projection_matrix": np.broadcast_to(
        #         self.viewprojection_matrices, (2, 4, 4)
        #     ),
        #     "view_matrix": np.broadcast_to(self.view_matrices, (2, 4, 4)),
        #     "vertex_areas": self.areas
        # }