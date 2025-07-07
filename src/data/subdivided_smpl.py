import pickle
import os
import torch
import numpy as np
import roma
import typing
from pathlib import Path
import logging
from pytorch3d.ops.subdivide_meshes import SubdivideMeshes
from pytorch3d.structures import Meshes
from moai.monads.geometry.mesh.calculate_normals import MeshVertexNormals
import trimesh

__all__ = ["SubdividedSMPL"]

log = logging.getLogger(__name__)

# NOTE: adapted from https://github.com/moverseai/rerun-animation


def _load_body_data(body_data_path: str) -> typing.Dict[str, np.ndarray]:
    with open(body_data_path, "rb") as f:
        body_data = pickle.load(f, encoding="latin1")
    shape_blendshapes = np.ascontiguousarray(
        np.array(body_data["shapedirs"]).astype(np.float32)
    )
    regressor = np.ascontiguousarray(
        np.array(body_data["J_regressor"].todense()).astype(np.float32)
    )
    parents = np.ascontiguousarray(
        np.array(body_data["kintree_table"]).astype(np.int32)
    )[0]
    template = np.ascontiguousarray(
        np.array(body_data["v_template"]).astype(np.float32)
    )
    weights = np.ascontiguousarray(np.array(body_data["weights"]).astype(np.float32))
    faces = np.ascontiguousarray(np.array(body_data["f"]).astype(np.int32))
    return shape_blendshapes, regressor, parents, template, faces, weights


def _rodrigues(axisangle: np.ndarray) -> np.ndarray:
    T = axisangle.shape[0]
    angle = np.linalg.norm(axisangle.reshape(-1, 3), ord=2, axis=-1) + 1e-8
    rot_dir = axisangle.reshape(-1, 3) / angle[:, np.newaxis]

    cos = np.cos(angle)[:, np.newaxis, np.newaxis]
    sin = np.sin(angle)[:, np.newaxis, np.newaxis]

    rx, ry, rz = np.split(rot_dir, 3, axis=1)
    K = np.zeros((3, 3), dtype=np.float32)

    zeros = np.zeros_like(rx)
    K = np.concatenate(
        [zeros, -rz, ry, rz, zeros, -rx, -ry, rx, zeros], axis=1
    ).reshape((-1, 3, 3))

    ident = np.eye(3, dtype=np.float32)[np.newaxis]
    rot_mat = ident + sin * K + (1 - cos) * (K @ K)
    return rot_mat.reshape(T, -1, 3, 3)


def _traverse_kinematic_chain(
    rotations: np.ndarray,
    joints: np.ndarray,
    parents: np.ndarray,
) -> np.ndarray:
    J = joints.shape[0]
    joints = joints[..., np.newaxis]

    rel_joints = joints.copy()
    rel_joints[1:] -= joints[parents[1:]]

    transforms_mat = np.tile(np.eye(4, dtype=np.float32), (J, 1, 1))
    transforms_mat[:, :3, :3] = rotations
    transforms_mat[:, :3, 3:4] = rel_joints

    transform_chain = [transforms_mat[0]]
    for c, p in enumerate(parents[1:], start=1):
        curr_res = transform_chain[p] @ transforms_mat[c]
        transform_chain.append(curr_res)
    transforms = np.stack(transform_chain, axis=0)

    posed_joints = transforms[:, :3, 3]

    transformed_joints = transforms[:, :3, :3] @ joints  # + transforms[..., :3, 3:4]
    relative_transforms = transforms.copy()
    relative_transforms[..., :3, 3] -= transformed_joints[..., 0]

    return posed_joints, relative_transforms


def _skinning(
    weights: np.ndarray,
    vertices: np.ndarray,
    relative_transforms: np.ndarray,
    normals: np.ndarray,
) -> np.ndarray:
    blended_transforms = weights @ relative_transforms.reshape(-1, 16)
    blended_transforms = blended_transforms.reshape(-1, 4, 4)
    posed_vertices = (blended_transforms[:, :3, :3] @ vertices[..., np.newaxis])[
        ..., 0
    ] + blended_transforms[:, :3, 3]
    posed_normals = blended_transforms[:, :3, :3] @ normals[..., np.newaxis]
    return posed_vertices, posed_normals, blended_transforms


def _create_projection_matrices(
    intrinsics: np.ndarray,
    width: int,
    height: int,
    znear: float = 0.01,
    zfar: float = 100.0,
):
    matrices = []
    for intr in intrinsics:
        focal_x, focal_y = intr[0, 0], intr[1, 1]
        cx, cy = intr[0, 2], intr[1, 2]
        # tanfovx=2.0 * np.arctan(width / (2.0 * focal_x))
        # tanfovy=2.0 * np.arctan(height / (2.0 * focal_y))
        tanfovx = width / (2.0 * focal_x)
        tanfovy = height / (2.0 * focal_y)
        # tanfovx=1.0 * np.arctan(width / (2.0 * focal_x))
        # tanfovy=1.0 * np.arctan(height / (2.0 * focal_y))
        # the origin at center of image plane
        top = tanfovy * znear
        bottom = -top
        right = tanfovx * znear
        left = -right
        # shift the frame window due to the non-zero principle point offsets
        offset_x = cx - (width / 2)
        offset_x = (offset_x / focal_x) * znear
        offset_y = cy - (height / 2)
        offset_y = (offset_y / focal_y) * znear

        top = top + offset_y
        left = left + offset_x
        right = right + offset_x
        bottom = bottom + offset_y

        P = np.zeros((4, 4)).astype(np.float32)
        z_sign = 1.0

        P[0, 0] = 2.0 * znear / (right - left)
        P[1, 1] = 2.0 * znear / (top - bottom)
        P[0, 2] = (right + left) / (right - left)
        P[1, 2] = (top + bottom) / (top - bottom)
        P[3, 2] = z_sign
        P[2, 2] = z_sign * zfar / (zfar - znear)
        P[2, 3] = -(zfar * znear) / (zfar - znear)
        matrices.append(P)
    return np.stack(matrices)


def _apply_offsets(
    vertices: torch.Tensor, faces: torch.Tensor, offsets: torch.Tensor
) -> torch.Tensor:
    normals = MeshVertexNormals().forward(
        vertices[np.newaxis],
        faces[np.newaxis],
    )["vectors"]
    return vertices + normals.numpy().squeeze() * offsets


def _subdivide(
    vertices: np.ndarray,
    faces: np.ndarray,
    features: np.ndarray,
    level=1,
    offsets=None,
) -> typing.Tuple[Meshes, torch.Tensor]:
    V, F, A = (
        torch.from_numpy(vertices),
        torch.from_numpy(faces),
        torch.from_numpy(features),
    )
    if offsets is not None and max(offsets.shape) == max(V.shape):
        V = _apply_offsets(V, F, offsets)
    for l in range(level):
        mesh = Meshes(V[np.newaxis], F[np.newaxis])
        subdiv, attrs = SubdivideMeshes()(
            mesh,
            feats=A,
        )
        V, F, A = subdiv.verts_packed(), subdiv.faces_packed(), attrs
        if offsets is not None and max(offsets.shape) == max(V.shape):
            V = _apply_offsets(V, F, offsets)
    # return subdiv, attrs
    return (
        subdiv.verts_packed(),
        subdiv.faces_packed(),
        subdiv.verts_normals_packed(),
        attrs,
    )


class SubdividedSMPL(torch.utils.data.Dataset):
    def __init__(
        self,
        path: str,
        gender: str,
        models_path: str,
        subset: typing.Optional[typing.Sequence[int]] = None,
        offsets_path: typing.Optional[str] = None,
        level: int = 1,
    ) -> None:
        super().__init__()
        body_data_path = os.path.join(
            models_path, "models", f"basicmodel_{gender[0]}_lbs_10_207_0_v1.1.0.pkl"
        )
        blendshapes, regressor, parents, template, faces, weights = _load_body_data(
            body_data_path
        )
        with np.load(Path(path) / "data.npz", allow_pickle=False) as data:
            for f in data.files:
                setattr(self, f, data[f])
        offsets = np.einsum(
            "vcb,b->vc", blendshapes[..., : self.betas.shape[-1]], self.betas
        )
        shaped = template + offsets
        shaped_joints = np.einsum("jv,vc->jc", regressor, shaped)
        extra_offsets = None
        if offsets_path and os.path.exists(offsets_path):
            extra_offsets = np.load(offsets_path)["offsets"]
            # normals = MeshVertexNormals().forward(
            #     torch.from_numpy(shaped)[np.newaxis],
            #     torch.from_numpy(faces)[np.newaxis],
            # )["vectors"]
            # shaped = shaped + normals.numpy().squeeze() * extra_offsets
        features = np.concatenate([regressor.T, weights], axis=-1)
        V, F, N, A = _subdivide(shaped, faces, features, level=level, offsets=extra_offsets)
        # mesh = Meshes(
        #     torch.from_numpy(shaped)[np.newaxis], torch.from_numpy(faces)[np.newaxis]
        # )
        # subdiv, attrs = SubdivideMeshes()(
        #     mesh,
        #     feats=torch.from_numpy(np.concatenate([regressor.T, weights], axis=-1)),
        # )
        J_regressor, skinning_weights = torch.split(
            A, shaped_joints.shape[0], dim=-1
        )
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
        self.areas = np.sqrt(vareas.numpy() / np.pi) / 3.5
        self.normals = torch.nn.functional.normalize(N, dim=-1).numpy()
        self.pose = _rodrigues(
            np.concatenate([self.global_orient[:, np.newaxis], self.pose], axis=1)
        )
        self.projection_matrices = _create_projection_matrices(
            self.intrinsics, 1920, 1080
        )  # TODO: fix hardcoded
        self.view_matrices = self.extrinsics.transpose(0, 2, 1).copy()  # row major
        self.viewprojection_matrices = (
            (self.projection_matrices @ self.extrinsics).transpose(0, 2, 1).copy()
        )
        self.camera_positions = np.linalg.inv(self.extrinsics)[:, :3, 3]

        self.subset = list(subset or range(len(self.extrinsics)))
        for s in self.subset:
            if s < 0 or s > len(self.extrinsics):
                msg = f"Subset index ({s}) is invalid."
                log.error(msg)
                raise RuntimeError(msg)

    def __len__(self) -> int:
        return len(self.time)

    def __getitem__(self, index) -> typing.Any:
        j, xf = _traverse_kinematic_chain(self.pose[index], self.joints, self.parents)
        v, n, bxf = _skinning(self.weights, self.vertices, xf, self.normals)
        Q = roma.rotmat_to_unitquat(torch.from_numpy(xf[:, :3, :3])).numpy()
        wQ = np.sqrt(self.weights[..., np.newaxis]) * Q[np.newaxis]
        evals, evecs = np.linalg.eigh(np.einsum("bki,bkj->bij", wQ, wQ))
        blended_quats = np.roll(evecs[..., -1], 1, axis=-1)  # XYZW -> WXYZ
        # blended_quats = evecs[..., -1]
        return {
            "shaped_joints": self.joints,
            "vertices": v + self.transl[index],
            "shaped": self.vertices,
            "normals": n.squeeze(),
            "blended_transforms": bxf,
            "skinning_weights": self.weights,
            "blended_rotations_quat": blended_quats,
            "faces": self.faces,
            "extrinsics": self.extrinsics[self.subset],  # .squeeze(),
            "intrinsics": self.intrinsics[self.subset],  # .squeeze(),
            "betas": self.betas,
            "pose": self.pose[index],
            "transl": self.transl[index],
            "global_orient": self.global_orient[index],
            "time": self.time[index],
            "camera_position": self.camera_positions[self.subset],
            "view_projection_matrix": self.viewprojection_matrices[self.subset],
            "view_matrix": self.view_matrices[self.subset],
            "vertex_areas": self.areas,
        }
