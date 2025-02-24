import logging
import os
import typing

import numpy as np
import plyfile
import torch
import trimesh
from moai.utils.arguments import ensure_path
from moai.monads.geometry.mesh.calculate_normals import MeshVertexNormals
from pytorch_lightning.callbacks import Callback

__all__ = ["SplatCloud"]

log = logging.getLogger(__name__)


class SplatCloud(
    Callback,
    typing.Callable[
        [typing.Dict[str, typing.Union[torch.Tensor, typing.Dict[str, torch.Tensor]]]],
        None,
    ],
):
    def __init__(
        self,
        path: str,
        method_type: str = "none",
    ):
        self.path = (
            ensure_path(log, "output folder", path) if os.path.isdir(path) else path
        )
        self.method_type = method_type

    def on_fit_end(
        self, trainer: "pl.Trainer", pl_module: "pl.LightningModule"
    ) -> None:
        """Called when fit ends."""
        if "parameter" in pl_module.named_flows["preproc"]:
            offsets = pl_module.named_flows["preproc"]["parameter"].value.cpu().detach()
        elif "named_params" in pl_module.named_flows["preproc"]:
            offsets = (
                pl_module.named_flows["preproc"]["named_params"].offsets.cpu().detach()
            )
        else:
            raise RuntimeError(
                "invalid configuration when using the Offsets exporter, expects either a single parameter or a `named` offset parameter."
            )
        offsets = offsets.numpy().squeeze()[..., np.newaxis]
        if hasattr(self, "shaped"):
            # m = trimesh.Trimesh(self.shaped, self.faces)
            # trimesh.Trimesh(self.shaped + m.vertex_normals * offsets, self.faces).export(
            #     os.path.join(self.path, "mesh.ply")
            #     if os.path.isdir(self.path)
            #     else self.path.replace(".npz", ".ply")
            # )
            _FLOWS_KEY_ = "nerf_preproc"  # 'nerf_postproc'
            assert _FLOWS_KEY_ in pl_module.named_flows
            assert "gaussian_splat_parameters" in pl_module.named_flows[_FLOWS_KEY_]
            gaussian_params = pl_module.named_flows[_FLOWS_KEY_][
                "gaussian_splat_parameters"
            ]
            sh = gaussian_params.spherical_harmonics_dc.detach().cpu()  # .squeeze()
            sh_dc = sh[..., 0:1, :]
            sh_rest = sh[..., 1:, :]
            if hasattr(gaussian_params, "spherical_harmonics_d1"):
                sh_rest = np.concatenate(
                    (
                        sh_rest,
                        gaussian_params.spherical_harmonics_d1.detach().cpu(),  # .squeeze(),
                    ),
                    axis=-2,
                )
                if hasattr(gaussian_params, "spherical_harmonics_d2"):
                    sh_rest = np.concatenate(
                        (
                            sh_rest,
                            gaussian_params.spherical_harmonics_d2.detach().cpu(),  # .squeeze(),
                        ),
                        axis=-2,
                    )
                    if hasattr(gaussian_params, "spherical_harmonics_d3"):
                        sh_rest = np.concatenate(
                            (
                                sh_rest,
                                gaussian_params.spherical_harmonics_d3.detach().cpu(),  # .squeeze(),
                            ),
                            axis=-2,
                        )
            quats = gaussian_params.rotation.detach().cpu().squeeze()
            scale = gaussian_params.scaling.detach().cpu().squeeze()
            opacity = gaussian_params.opacity.detach().cpu().squeeze()[..., np.newaxis]
            sxyz = self.shaped
            # xyz = self.shaped + self.normals * offsets
            # nxyz = self.normals
            nxyz = MeshVertexNormals()(
                torch.from_numpy(self.shaped)[np.newaxis],
                torch.from_numpy(self.faces[np.newaxis]),
            )["vectors"][0].numpy()
            xyz = self.shaped + nxyz * offsets
            W = self.skinning_weights
            l1 = [
                "x",
                "y",
                "z",
                "nx",
                "ny",
                "nz",
                "f_dc_0",
                "f_dc_1",
                "f_dc_2",
            ]
            l2 = [f"f_rest_{i}" for i in range(45)]
            l3 = [
                "opacity",
                "scale_0",
                "scale_1",
                "scale_2",
                "rot_0",
                "rot_1",
                "rot_2",
                "rot_3",
                # "sx",
                # "sy",
                # "sz",
            ]
            l = l1 + l2 + l3
            dtype_full = [(attribute, "f4") for attribute in l]
            elements = np.empty(xyz.shape[0], dtype=dtype_full)
            sh_rest = np.concatenate(
                (sh_rest, np.zeros((*sh_rest.shape[:2], 15 - sh_rest.shape[-2], 3))), axis=-2
            )
            attributes = np.concatenate(
                # (xyz, nxyz, sh_dc, opacity, scale, quats, sxyz), axis=-1
                (xyz, nxyz, sh_dc.squeeze(), sh_rest.squeeze().reshape(-1, 45), opacity, scale, quats),
                axis=-1,
            )
            elements[:] = list(map(tuple, attributes))
            el = plyfile.PlyElement.describe(elements, "vertex")
            plyfile.PlyData([el]).write("splat.ply")
            ##### JOINTS
            trimesh.PointCloud(self.shaped_joints).export("joints.ply")
            ##### SKINNED MESH
            F = np.empty(len(self.faces), dtype=[("vertex_indices", "i4", (3,))])
            F["vertex_indices"] = self.faces
            V = np.empty(
                xyz.shape[0],
                dtype=[("x", "f4"), ("y", "f4"), ("z", "f4")]
                + [(f"s{i}", "f4") for i in range(W.shape[-1])],
            )
            V[:] = list(map(tuple, np.concatenate((self.shaped, W), axis=-1)))
            data = plyfile.PlyData(
                [
                    plyfile.PlyElement.describe(
                        V, "vertex", comments=[self.method_type]
                    ),
                    plyfile.PlyElement.describe(F, "face"),
                ]
            )
            data.write("skinned_mesh.ply")

    def _cache_tensor(self, key: str, tensors: typing.Mapping[str, typing.Any]) -> None:
        if key in tensors and not hasattr(self, key):
            setattr(self, key, tensors[key].detach().cpu().numpy().squeeze())

    def __call__(
        self,
        tensors: typing.Mapping[str, torch.Tensor],
        batch_idx: typing.Optional[int] = None,
        epoch: typing.Optional[int] = None,
    ) -> None:
        self._cache_tensor("shaped", tensors)
        self._cache_tensor("shaped_joints", tensors)
        self._cache_tensor("skinning_weights", tensors)
        self._cache_tensor("faces", tensors)
        # if "shaped" in tensors and not hasattr(self, "shaped"):
        #     self.shaped = tensors["shaped"].detach().cpu().numpy().squeeze()
        # if "shaped_joints" in tensors and not hasattr(self, "shaped_joints"):
        #     self.shaped_joints = tensors["shaped_joints"].detach().cpu().numpy().squeeze()
        # # if "original_vertex_normals" in tensors and not hasattr(self, "normals"):
        # #     self.normals = (
        # #         tensors["original_vertex_normals.vectors"]
        # #         .detach()
        # #         .cpu()
        # #         .numpy()
        # #         .squeeze()
        # #     )
        # if "skinning_weights" in tensors and not hasattr(self, "weights"):
        #     self.weights = tensors["skinning_weights"].detach().cpu().numpy().squeeze()
        # if "faces" in tensors and not hasattr(self, "faces"):
        #     self.faces = tensors["faces"].detach().cpu().numpy().squeeze()
