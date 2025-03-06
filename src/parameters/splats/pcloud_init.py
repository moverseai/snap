import numpy as np
import os
import logging
import plyfile

import torch

log = logging.getLogger(__name__)

__all__ = ["InitializeSplats"]


class InitializeSplats(object):
    def __init__(self, data_path: str):
        self.data_path = data_path

    def __call__(self, model: torch.nn.Module) -> None:
        log.info(f"Initializing animated splats from {self.data_path}.")
        data = np.load(os.path.join(self.data_path, "offsets.npz"))
        model.named_flows.preproc.named_params.offsets.data.copy_(
            torch.from_numpy(data["offsets"])
        )
        with open(os.path.join(self.data_path, "splat.ply"), "rb") as f:
            ply = plyfile.PlyData.read(f)
        # x = ply['vertex']['x']
        # y = ply['vertex']['y']
        # z = ply['vertex']['z']
        sh0, sh1, sh2 = (
            ply["vertex"]["f_dc_0"],
            ply["vertex"]["f_dc_1"],
            ply["vertex"]["f_dc_2"],
        )
        q0, q1, q2, q3 = (
            ply["vertex"]["rot_0"],
            ply["vertex"]["rot_1"],
            ply["vertex"]["rot_2"],
            ply["vertex"]["rot_3"],
        )
        s0, s1, s2 = (
            ply["vertex"]["scale_0"],
            ply["vertex"]["scale_1"],
            ply["vertex"]["scale_2"],
        )
        opacity = ply["vertex"]["opacity"]
        model.named_flows.nerf_preproc.gaussian_splat_parameters.opacity.data.copy_(
            torch.from_numpy(opacity[np.newaxis, :, np.newaxis])
        )
        model.named_flows.nerf_preproc.gaussian_splat_parameters.rotation.data.copy_(
            torch.from_numpy(np.stack((q0, q1, q2, q3), axis=-1))
        )
        model.named_flows.nerf_preproc.gaussian_splat_parameters.scaling.data.copy_(
            torch.from_numpy(np.stack((s0, s1, s2), axis=-1))
        )
        model.named_flows.nerf_preproc.gaussian_splat_parameters.spherical_harmonics_dc.data.copy_(
            torch.from_numpy(
                np.stack((sh0, sh1, sh2), axis=-1)[np.newaxis, :, np.newaxis]
            )
        )
        if hasattr(
            model.named_flows.nerf_preproc.gaussian_splat_parameters,
            "spherical_harmonics_d1",
        ):
            d1 = []
            for i in range(3, 12):
                d1.append(ply["vertex"][f"f_rest_{i}"])
            model.named_flows.nerf_preproc.gaussian_splat_parameters.spherical_harmonics_d1.data.copy_(
                torch.from_numpy(np.stack(d1, axis=-1).reshape(-1, 3, 3)[np.newaxis])
            )
            if hasattr(
                model.named_flows.nerf_preproc.gaussian_splat_parameters,
                "spherical_harmonics_d2",
            ):
                d2 = []
                for i in range(12, 27):
                    d2.append(ply["vertex"][f"f_rest_{i}"])
                model.named_flows.nerf_preproc.gaussian_splat_parameters.spherical_harmonics_d2.data.copy_(
                    torch.from_numpy(
                        np.stack(d2, axis=-1).reshape(-1, 5, 3)[np.newaxis]
                    )
                )
                if hasattr(
                    model.named_flows.nerf_preproc.gaussian_splat_parameters,
                    "spherical_harmonics_d3",
                ):
                    d3 = []
                    for i in range(28, 49):
                        d3.append(ply["vertex"][f"f_rest_{i}"])
                    model.named_flows.nerf_preproc.gaussian_splat_parameters.spherical_harmonics_d3.data.copy_(
                        torch.from_numpy(
                            np.stack(d3, axis=-1).reshape(-1, 7, 3)[np.newaxis]
                        )
                    )
        log.info(f"Initialized {len(opacity)} splats.")
