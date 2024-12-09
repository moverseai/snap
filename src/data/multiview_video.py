import typing
from pathlib import Path

import cv2
import numpy as np
import torch

__all__ = ['MultiviewVideo']

class MultiviewVideo(torch.utils.data.Dataset):
    def __init__(self, path: str) -> None:
        super().__init__()
        self.videos = []
        for i, vf in enumerate(sorted(Path(path).glob("*.mp4"))):
            self.videos.append(cv2.VideoCapture(str(vf)))
            self.num_frames = int(self.videos[-1].get(cv2.CAP_PROP_FRAME_COUNT))

    def __len__(self) -> int:
        return self.num_frames
    
    def __getitem__(self, index) -> typing.Any:
        imgs = []
        for vid in self.videos:
            vid.set(cv2.CAP_PROP_POS_FRAMES, index)
            ok, frame = vid.read()
            imgs.append(np.flip(frame, -1).transpose(2, 0, 1).astype(np.float32) / 255.0)
        return { 'color': np.stack(imgs)}