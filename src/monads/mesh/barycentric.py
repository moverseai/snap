import torch

__all__ = ["BarycentricInterpolation"]


class BarycentricInterpolation(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(
        self,
        attributes: torch.Tensor,
        faces: torch.Tensor,
        triangles: torch.Tensor,
        weights: torch.Tensor,
    ) -> torch.Tensor:
        interpolated = attributes * weights
        if weights.shape[-1] != 3:
            total = weights.sum(-1, keepdim=True)
            remaining = 1.0 - total
            interpolated = torch.cat([interpolated, attributes * remaining], dim=-1)
        return {
            "interpolated": interpolated.sum(-1, keepdim=True),
            "weighted": interpolated,
        }
