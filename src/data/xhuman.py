import glob
import toolz
import cv2
import pickle
import os
import torch
import numpy as np
import roma
import typing
import logging
from collections import defaultdict
import trimesh

__all__ = ["XHuman"]

log = logging.getLogger(__name__)

# from subdivided_smpl import (
from src.data.subdivided_smpl import (
    _subdivide,
    _rodrigues,
    _create_projection_matrices,
    _traverse_kinematic_chain,
    _skinning,
)


def _load_expressive_body_data(body_data_path: str) -> typing.Dict[str, np.ndarray]:
    body_data = np.load(body_data_path)
    shape_blendshapes = np.ascontiguousarray(
        np.array(body_data["shapedirs"]).astype(np.float32)
    )
    regressor = np.ascontiguousarray(
        np.array(body_data["J_regressor"]).astype(np.float32)
    )
    parents = np.ascontiguousarray(
        np.array(body_data["kintree_table"]).astype(np.int32)
    )[0]
    template = np.ascontiguousarray(
        np.array(body_data["v_template"]).astype(np.float32)
    )
    weights = np.ascontiguousarray(np.array(body_data["weights"]).astype(np.float32))
    faces = np.ascontiguousarray(np.array(body_data["f"]).astype(np.int32))
    hands_meanr = np.ascontiguousarray(
        np.array(body_data["hands_meanr"]).astype(np.int32)
    )
    hands_meanl = np.ascontiguousarray(
        np.array(body_data["hands_meanl"]).astype(np.int32)
    )
    return (
        shape_blendshapes,
        regressor,
        parents,
        template,
        faces,
        weights,
        hands_meanl,
        hands_meanr,
    )


class XHuman(torch.utils.data.Dataset):
    _METADATA_ = {
        "00016": {
            "gender": "male",
        },
        "00019": {
            "gender": "female",
        },
        "00034": {
            "gender": "male",
        },        
        "00028": {
            "gender": "male",
        },
        "00087": {
            "gender": "male",
        }
    }

    def __init__(
        self,
        path: str,
        subject: str,
        split: str,
        take: str,
        models_path: str,
        offsets_path: typing.Optional[str] = None,
        level: int = 1,
        batch: int = 2,
    ) -> None:
        super().__init__()
        gender = XHuman._METADATA_[subject]["gender"]
        body_data_path = os.path.join(
            models_path,
            "models",
            "smplx",
            f"SMPLX_{gender.upper()}.npz",
        )
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
        self.pose_mean = np.concatenate(
            [
                np.zeros(3, dtype=np.float32),
                np.zeros(21 * 3, dtype=np.float32),
                np.zeros(3, dtype=np.float32),
                np.zeros(3, dtype=np.float32),
                np.zeros(3, dtype=np.float32),
                left_hand_mean,
                right_hand_mean,
            ],
            axis=0,
        )
        self.data_path = os.path.join(path, subject, split, take)
        cams = np.load(os.path.join(self.data_path, "render", "cameras.npz"))
        self.intrinsic = cams["intrinsic"].astype(np.float32)
        self.extrinsic = cams["extrinsic"].astype(np.float32)
        self.batch = batch
        imgs = glob.glob(os.path.join(path, subject, split, take, "render", "image", "*.??g"))
        indices = [x for x in map(int, map(lambda p: os.path.splitext(os.path.basename(p))[0].split("_")[1], imgs))]
        perm = np.random.permutation(len(indices))
        self.file_indices = np.array(indices)[perm]
        self.indices = np.array(list(range(len(self.file_indices))))[perm]
        # self.indices = np.random.permutation(len(self.extrinsic))
        with open(
            os.path.join(self.data_path, "smplx", "mesh-f00001_smplx.pkl"), "rb"
        ) as f:
            data = pickle.load(f)
        self.betas = data["betas"]
        offsets = np.einsum(
            "vcb,b->vc", blendshapes[..., : self.betas.shape[-1]], self.betas
        )
        self.expression_blendshapes = blendshapes[..., 300:]
        shaped = template + offsets
        shaped_joints = np.einsum("jv,vc->jc", regressor, shaped)
        extra_offsets = None
        if offsets_path and os.path.exists(offsets_path):
            extra_offsets = np.load(offsets_path)["offsets"]
        #     normals = MeshVertexNormals().forward(
        #         torch.from_numpy(shaped)[np.newaxis],
        #         torch.from_numpy(faces)[np.newaxis],
        #     )["vectors"]
        #     shaped = shaped + normals.numpy().squeeze() * extra_offsets
        features = np.concatenate([regressor.T, weights], axis=-1)
        # subdiv, attrs = _subdivide(shaped, faces, features, level=level, offsets=extra_offsets)
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
        # self.pose = _rodrigues(
        #     np.concatenate([self.global_orient[:, np.newaxis], self.pose], axis=1)
        # )
        self.projection_matrices = _create_projection_matrices(
            self.intrinsic[np.newaxis], 800, 1200
        )  # TODO: fix hardcoded
        # self.view_matrices = self.extrinsics.transpose(0, 2, 1).copy()  # row major
        # self.viewprojection_matrices = (
        #     (self.projection_matrices @ self.extrinsics).transpose(0, 2, 1).copy()
        # )
        # self.camera_positions = np.linalg.inv(self.extrinsics)[:, :3, 3]

    def __len__(self) -> int:
        # return int(len(self.extrinsic) / self.batch) - int(
        #     len(self.extrinsic) % self.batch
        # )
        return int(len(self.indices) / self.batch) - int(
            len(self.indices) % self.batch
        )

    def _load_sample(self, batched: dict, index: int, file_index: int) -> None:
        with open(
            os.path.join(self.data_path, "smplx", f"mesh-f{(file_index):05d}_smplx.pkl"),
            "rb",
        ) as f:
            data = pickle.load(f)
        full_pose = np.concatenate(
            [
                data["global_orient"],
                data["body_pose"],
                data["jaw_pose"],
                data["leye_pose"],
                data["reye_pose"],
                data["right_hand_pose"],
                data["left_hand_pose"],
                # data["left_hand_pose"],
                # data["right_hand_pose"],
            ],
            axis=0,
        )
        # full_pose += self.pose_mean
        pose = _rodrigues(full_pose[np.newaxis])
        j, xf = _traverse_kinematic_chain(pose, self.joints, self.parents)
        expression = data["expression"]
        # offsets = np.einsum(
        #     "vcb,b->vc",
        #     self.expression_blendshapes[..., : expression.shape[-1]],
        #     expression,
        # )  # NOTE: can't happen till we upsample expressions
        vertices = self.vertices  #  + offsets1
        v, n, bxf = _skinning(self.weights, vertices, xf, self.normals)
        Q = roma.rotmat_to_unitquat(torch.from_numpy(xf[:, :3, :3])).numpy()
        wQ = np.sqrt(self.weights[..., np.newaxis]) * Q[np.newaxis]
        evals, evecs = np.linalg.eigh(np.einsum("bki,bkj->bij", wQ, wQ))
        blended_quats = np.roll(evecs[..., -1], 1, axis=-1)  # XYZW -> WXYZ
        # blended_quats = evecs[..., -1]
        view_matrices = self.extrinsic[index].transpose(1, 0).copy()  # row major
        viewprojection_matrices = (
            (self.projection_matrices[0] @ self.extrinsic[index]).transpose(1, 0).copy()
        )
        camera_position = np.linalg.inv(self.extrinsic[index])[:3, 3]
        img = cv2.imread(
            os.path.join(
                self.data_path, "render", "image", f"color_{(file_index):06d}.png"
            )
        )
        img = np.flip(img, -1).transpose(2, 0, 1).astype(np.float32) / 255.0
        msk = cv2.imread(
            os.path.join(
                self.data_path, "render", "depth", f"depth_{(file_index):06d}.tiff"
            ),
            cv2.IMREAD_ANYDEPTH,
        )
        msk = (msk < 10.0).astype(np.float32)[np.newaxis]
        batched["vertices"].append(v + data["transl"])
        batched["shaped"].append(vertices)
        batched["normals"].append(n.squeeze())
        batched["blended_transforms"].append(bxf)
        batched["blended_rotations_quat"].append(blended_quats)
        batched["extrinsics"].append(self.extrinsic[index])
        batched["pose"].append(pose[0])
        batched["transl"].append(data["transl"])
        batched["global_orient"].append(data["global_orient"])
        batched["time"].append(index / len(self.extrinsic))
        batched["camera_position"].append(camera_position)
        batched["view_projection_matrix"].append(viewprojection_matrices)
        batched["view_matrix"].append(view_matrices)
        batched["color"].append(img)
        batched["mask"].append(msk)

    def __getitem__(self, index: int) -> typing.Any:
        # i1 = int(self.indices[index * self.batch])
        # i2 = int(self.indices[i1 + 1])

        batched = defaultdict(list)
        for i in range(self.batch):
            idx = int(self.indices[index * self.batch + i])
            f_idx = int(self.file_indices[index * self.batch + i])
            self._load_sample(batched, idx, f_idx)

        returned = toolz.valmap(lambda v: np.stack(v), batched)
        returned["shaped_joints"] = self.joints
        returned["shaped"] = returned["shaped"][0]
        returned["skinning_weights"] = self.weights
        returned["faces"] = self.faces
        returned["intrinsics"] = np.broadcast_to(self.intrinsic, (self.batch, 3, 3))
        returned["vertex_areas"] = self.areas # np.broadcast_to(self.areas, (self.batch, *self.areas.shape))
        returned["betas"] = self.betas
        return returned
