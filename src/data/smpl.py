import torch
import numpy as np
import typing
from pathlib import Path
import logging

__all__ = ["SMPL"]

log = logging.getLogger(__name__)

class SMPL(torch.utils.data.Dataset):
    def __init__(
        self, path: str, subset: typing.Optional[typing.Sequence[int]] = None
    ) -> None:
        super().__init__()
        with np.load(Path(path) / "data.npz", allow_pickle=False) as data:
            for f in data.files:
                setattr(self, f, data[f])
        self.subset = list(subset or range(len(self.extrinsics)))
        for s in self.subset:
            if s < 0 or s > len(self.extrinsics):
                msg = f"Subset index ({s}) is invalid."
                log.error(msg)
                raise RuntimeError(msg)

    def __len__(self) -> int:
        return len(self.time)

    def __getitem__(self, index) -> typing.Any:
        return {
            "extrinsics": self.extrinsics[self.subset],#.squeeze(),
            "intrinsics": self.intrinsics[self.subset],#.squeeze(),
            "betas": self.betas,
            "pose": self.pose[index],
            "transl": self.transl[index],
            "global_orient": self.global_orient[index],
            "time": self.time[index],
        }
