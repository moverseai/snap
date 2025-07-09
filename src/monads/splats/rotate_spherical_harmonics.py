import torch
from e3nn import o3
import typing

__all__ = ["RotateSphericalHarmonics"]


class RotateSphericalHarmonics(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.register_buffer("axis_flip",
            torch.tensor([[[[0, 0, 1], [1, 0, 0], [0, 1, 0]]]]).float()
        )
        self.register_buffer("axis_flip_inv",
            torch.linalg.inv(self.axis_flip)
        )

    def forward(
        self,
        rotations: torch.Tensor,  # [(B), N, 3, 3]
        sh1: torch.Tensor,  # [(B), N, 3, 3]
        sh2: typing.Optional[torch.Tensor] = None,  # [(B), N, 5, 3],
        sh3: typing.Optional[torch.Tensor] = None,  # [(B), N, 7, 7]
    ) -> typing.Dict[str, torch.Tensor]:
        F = self.axis_flip if len(rotations.shape) > 3 else self.axis_flip[0]
        iF = self.axis_flip_inv if len(rotations.shape) > 3 else self.axis_flip_inv[0]
        R = iF.expand_as(rotations) @ rotations @ F.expand_as(rotations)
        angles = o3.matrix_to_angles(R)
        D_1 = o3.wigner_D(1, angles[0], angles[1], angles[2])
        ret = { 'sh1': D_1 @ sh1}
        if sh2 is not None:
            D_2 = o3.wigner_D(2, angles[0], angles[1], angles[2])
            ret['sh2'] = D_2 @ sh2
            if sh3 is not None:
                D_3 = o3.wigner_D(3, angles[0], angles[1], angles[2])
                ret['sh3'] = D_3 @ sh3
        return ret
