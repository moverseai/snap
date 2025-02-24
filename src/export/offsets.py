import logging
import os
import typing

import numpy as np
import torch
import trimesh
from moai.utils.arguments import ensure_path
from pytorch_lightning.callbacks import Callback

__all__ = ["Offsets"]

log = logging.getLogger(__name__)


class Offsets(
    Callback,
    typing.Callable[
        [typing.Dict[str, typing.Union[torch.Tensor, typing.Dict[str, torch.Tensor]]]],
        None,
    ],
):
    def __init__(
        self,
        path: str,
    ):
        self.path = (
            ensure_path(log, "output folder", path) if os.path.isdir(path) else path
        )

    def on_fit_end(
        self, trainer: "pl.Trainer", pl_module: "pl.LightningModule"
    ) -> None:
        """Called when fit ends."""
        if 'parameter' in pl_module.named_flows['preproc']:
            offsets = (
                pl_module.named_flows["preproc"]["parameter"].value.cpu().detach().numpy()
            )
        elif 'named_params' in pl_module.named_flows['preproc']:
            offsets = (
                pl_module.named_flows["preproc"]["named_params"].offsets.cpu().detach().numpy()
            )
        else:
            raise RuntimeError("invalid configuration when using the Offsets exporter, expects either a single parameter or a `named` offset parameter.")
        np.savez_compressed(
            (
                os.path.join(self.path, "offsets.npz")
                if os.path.isdir(self.path)
                else self.path
            ),
            offsets=offsets,
        )
        if hasattr(self, "shaped"):
            m = trimesh.Trimesh(self.shaped, self.faces)
            trimesh.Trimesh(self.shaped + m.vertex_normals * offsets, self.faces).export(
                os.path.join(self.path, "mesh.ply")
                if os.path.isdir(self.path)
                else self.path.replace(".npz", ".ply")
            )

    def __call__(
        self,
        tensors: typing.Mapping[str, torch.Tensor],
        batch_idx: typing.Optional[int] = None,
        epoch: typing.Optional[int] = None,
    ) -> None:
        if "shaped" in tensors and not hasattr(self, "shaped"):
            self.shaped = tensors["shaped"].detach().cpu().numpy().squeeze()
        if "faces" in tensors and not hasattr(self, "faces"):
            self.faces = tensors["faces"].detach().cpu().numpy().squeeze()
