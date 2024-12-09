import torch
import numpy as np
import typing
from pathlib import Path

__all__ = ['SMPL']

class SMPL(torch.utils.data.Dataset):
    def __init__(self, path: str) -> None:
        super().__init__()
        with np.load(Path(path) / "data.npz", allow_pickle=False) as data:
            for f in data.files:
                setattr(self, f, data[f])

    def __len__(self) -> int:
        return len(self.time)
    
    def __getitem__(self, index) -> typing.Any:
        return {
            'extrinsics': self.extrinsics,
            'intrinsics': self.intrinsics,
            'betas': self.betas,
            'pose': self.pose[index],
            'transl': self.transl[index],
            'global_orient': self.global_orient[index],
            'time': self.time[index],
        }