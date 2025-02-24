import torch

__all__ = ['ExpandBatched']

class ExpandBatched(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor: torch.Tensor, expand: torch.Tensor) -> torch.Tensor:
        unbatched_dims = expand.shape[1:]
        for _ in range(len(unbatched_dims) - len(tensor.shape) + 1):
            tensor = tensor.unsqueeze(-1)
        return tensor.expand(-1, *unbatched_dims)