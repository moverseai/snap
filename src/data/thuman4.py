import toolz
from collections import defaultdict
import json
import glob
import typing
from pathlib import Path
import os
import cv2
import numpy as np
import torch
import logging
import roma
import trimesh

from src.data.xhuman import (
    _load_expressive_body_data,
    _subdivide,
    _rodrigues,
    _create_projection_matrices,
    _traverse_kinematic_chain,
    _skinning,
)

__all__ = ["THuman4"]


log = logging.getLogger(__name__)


class THuman4(torch.utils.data.Dataset):
    # _SPLITS_ = {
    #     "male-4-casual": {
    #         "train": (0, 659, 6),
    #         "val": (660, 660, 6),
    #         "test": (660, 872, 6),
    #         "gender": "male",
    #     },
    #     "male-3-casual": {
    #         "train": (0, 455, 4),
    #         "val": (456, 456, 4),
    #         "test": (456, 675, 4),
    #         "gender": "male",
    #     },
    # }

    def _extract_missing_frames(
        self, root: str, subject: str, views: typing.Sequence[int]
    ) -> typing.Set[str]:
        with open(os.path.join(root, subject, "missing_img_files.txt")) as f:
            imgs = f.readlines()
        with open(os.path.join(root, subject, "missing_msk_files.txt")) as f:
            msks = f.readlines()
        camviews = [f"cam{v:02d}" for v in views]
        missing_frames = set()
        for fn in imgs + msks:
            *parts, cam, frame = Path(fn).parts
            if cam in camviews:
                missing_frames.add(os.path.splitext(frame)[0])
        return missing_frames

    def __init__(
        self,
        path: str,
        subject: str,
        models_path: str,
        level: int = 1,
        views: typing.Sequence[int] = [0, 6, 12, 18],
        offsets_path: typing.Optional[str]=None,
    ) -> None:
        super().__init__()
        self.path = path
        self.subject = subject
        missing_frames = self._extract_missing_frames(path, subject, views)
        self.views = views
        self.frames = []
        for v in views:
            imgs = glob.glob(
                os.path.join(path, subject, "images", f"cam{v:02d}", "*.??g")
            )
            msks = glob.glob(
                os.path.join(path, subject, "masks", f"cam{v:02d}", "*.??g")
            )
            for fn in imgs + msks:
                frame = os.path.splitext(Path(fn).parts[-1])[0]
                if frame not in missing_frames:
                    self.frames.append(frame)
        with open(os.path.join(path, subject, "calibration.json"), "r") as f:
            calib = json.load(f)
        self.extrinsics = np.zeros((len(views), 4, 4))
        self.extrinsics[:, 3, 3] = 1.0
        self.intrinsics = np.zeros((len(views), 3, 3))
        for i, v in enumerate(views):
            cam = f"cam{v:02d}"  # 1330, 1150
            self.intrinsics[i] = np.array(calib[cam]["K"]).reshape(3, 3)
            self.extrinsics[i, :3, :3] = np.array(calib[cam]["R"]).reshape(3, 3)
            self.extrinsics[i, :3, 3] = np.array(calib[cam]["T"])

        perm = np.random.permutation(len(self.frames)).tolist()
        self.frames = [self.frames[i] for i in perm]  # self.frames[perm]
        body_data_path = os.path.join(models_path, "models", "smplx", f"SMPLX_MALE.npz")
        (
            blendshapes,
            regressor,
            parents,
            template,
            faces,
            weights,
            left_hand_mean,
            right_hand_mean,
        ) = _load_expressive_body_data(body_data_path)
        data = np.load(Path(path) / subject / f"smpl_params.npz")
        self.betas = data["betas"].squeeze()
        offsets = np.einsum(
            "vcb,b->vc", blendshapes[..., : self.betas.shape[-1]], self.betas
        )
        self.expression_blendshapes = blendshapes[..., 300:]
        shaped = template + offsets
        shaped_joints = np.einsum("jv,vc->jc", regressor, shaped)
        extra_offsets = None
        if offsets_path and os.path.exists(offsets_path):
            extra_offsets = np.load(offsets_path)["offsets"]
        features = np.concatenate([regressor.T, weights], axis=-1)
        V, F, N, A = _subdivide(shaped, faces, features, level=level, offsets=extra_offsets)
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
        self.transl = data["transl"]
        self.global_orient = data["global_orient"]
        self.pose = data["body_pose"]
        self.expression = data["expression"]
        self.jaw_pose = data["jaw_pose"]
        self.left_hand_pose = data["left_hand_pose"]
        self.right_hand_pose = data["right_hand_pose"]
        # self.pose = _rodrigues(
        #     np.concatenate([self.global_orient[:, np.newaxis], self.pose], axis=1)
        # )
        self.projection_matrices = _create_projection_matrices(
            self.intrinsics, 1330, 1150
        )
        self.view_matrices = self.extrinsics.transpose(0, 2, 1).copy()  # row major
        self.viewprojection_matrices = (
            (self.projection_matrices @ self.extrinsics).transpose(0, 2, 1).copy()
        )
        self.camera_positions = np.linalg.inv(self.extrinsics)[:, :3, 3]

    def __len__(self) -> int:
        # return int(len(self.frames) / 2) - int(len(self.frames % 2))
        return len(self.frames)

    def __getitem__(self, index) -> typing.Any:
        frame = self.frames[index]
        result = defaultdict(list)
        for v in self.views:
            img_fn = os.path.join(
                self.path, self.subject, "images", f"cam{v:02d}", f"{frame}.jpg"
            )
            msk_fn = os.path.join(
                self.path, self.subject, "masks", f"cam{v:02d}", f"{frame}.jpg"
            )
            result["color"].append(
                np.flip(cv2.imread(img_fn), -1).transpose(2, 0, 1).astype(np.float32) / 255.0
            )
            result["mask"].append(
                cv2.imread(msk_fn, cv2.IMREAD_ANYDEPTH)[np.newaxis].astype(np.float32) / 255.0
            )
            frm_idx = int(frame)
            result["time"].append(torch.scalar_tensor(frm_idx / 2500.0).float())
            full_pose = np.concatenate(
                [
                    self.global_orient[frm_idx],
                    self.pose[frm_idx],
                    self.jaw_pose[frm_idx],
                    np.zeros(3),
                    np.zeros(3),
                    self.left_hand_pose[frm_idx],
                    self.right_hand_pose[frm_idx],                
                ],
                axis=0,
            )
            pose = _rodrigues(full_pose[np.newaxis])
            j, xf = _traverse_kinematic_chain(pose, self.joints, self.parents)
            v, n, bxf = _skinning(self.weights, self.vertices, xf, self.normals)
            Q = roma.rotmat_to_unitquat(torch.from_numpy(xf[:, :3, :3])).numpy()
            wQ = np.sqrt(self.weights[..., np.newaxis]) * Q[np.newaxis]
            evals, evecs = np.linalg.eigh(np.einsum("bki,bkj->bij", wQ, wQ))
            blended_quats = np.roll(evecs[..., -1], 1, axis=-1)  # XYZW -> WXYZ
            # blended_quats1 = evecs1[..., -1]
            result["vertices"].append(v + self.transl[frm_idx])
            result["normals"].append(n.squeeze())
            result["blended_transforms"].append(bxf)
            result["blended_rotations_quat"].append(blended_quats)
            result["pose"].append(pose[0].astype(np.float32))
            result["transl"].append(self.transl[frm_idx])
            result["global_orient"].append(self.global_orient[frm_idx])

        result["shaped"] = self.vertices
        result["shaped_joints"] = self.joints
        result["extrinsics"] = self.extrinsics.astype(np.float32)
        result = toolz.valmap(lambda x: np.stack(x), result)
        result["view_matrix"] = self.view_matrices.astype(np.float32)
        result["view_projection_matrix"] = self.viewprojection_matrices.astype(np.float32)
        result["camera_position"] = self.camera_positions.astype(np.float32)
        result["intrinsics"] = self.intrinsics.astype(np.float32)
        result["betas"] = self.betas
        result["faces"] = self.faces
        result["skinning_weights"] = self.weights
        result["vertex_areas"] = self.areas # np.broadcast_to(self.areas, (self.batch, *self.areas.shape))
        return result

