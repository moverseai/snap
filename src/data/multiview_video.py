import typing
from pathlib import Path

import cv2
import numpy as np
import torch
import logging

__all__ = ["MultiviewVideo", "MultiviewMaskVideo"]


log = logging.getLogger(__name__)

import re
from pathlib import Path

def _extract_index(path: Path) -> int:    
    """
    Extracts an index from the filename stem of the given path. 
    """
    match = re.search(r'(\d+)', path.stem)
    return int(match.group(1)) if match else -1

class MultiviewVideo(torch.utils.data.Dataset):
    def __init__(
        self, 
        path: str, 
        prefix: str='',
        suffix: str='',
        extension: str='mp4',
        subset: typing.Optional[typing.Sequence[int]] = None
    ) -> None:
        super().__init__()
        self.videos = []
        video_files = sorted(Path(path).glob(f"{prefix}*{suffix}.{extension}"), key=_extract_index)
        self.subset = list(subset or range(len(video_files)))
        for s in self.subset:
            if s < 0 or s > len(video_files):
                msg = f"Subset index ({s}) is invalid."
                log.error(msg)
                raise RuntimeError(msg)
        self.num_frames = 60 * 60 * 60 # 1hour @ 60fps
        for i, id in enumerate(self.subset):
            self.videos.append(cv2.VideoCapture(str(video_files[id])))
            num_frames = int(self.videos[-1].get(cv2.CAP_PROP_FRAME_COUNT))
            self.num_frames = min(num_frames, self.num_frames)

    def __len__(self) -> int:
        return self.num_frames

    def __getitem__(self, index) -> typing.Any:
        imgs, times, views = [], [], []
        for view, vid in zip(self.subset, self.videos):
            vid.set(cv2.CAP_PROP_POS_FRAMES, index)
            ok, frame = vid.read()
            imgs.append(
                np.flip(frame, -1).transpose(2, 0, 1).astype(np.float32) / 255.0
            )
            times.append(np.array(index / self.num_frames).astype(np.float32))
            views.append(np.array(view / len(self.subset)).astype(np.float32)) 
        return {"color": np.stack(imgs), 'time': np.stack(times), 'views': np.stack(views)}


class MultiviewMaskVideo(torch.utils.data.Dataset):
    def __init__(
        self, 
        path: str, 
        prefix: str='',
        suffix: str='',
        extension: str='mp4',
        subset: typing.Optional[typing.Sequence[int]] = None,        
    ) -> None:
        super().__init__()
        self.videos = []
        video_files = sorted(Path(path).glob(f"{prefix}*{suffix}.{extension}"), key=_extract_index)
        self.subset = list(subset or range(len(video_files)))
        for s in self.subset:
            if s < 0 or s > len(video_files):
                msg = f"Subset index ({s}) is invalid."
                log.error(msg)
                raise RuntimeError(msg)
        self.num_frames = 60 * 60 * 60 # 1hour @ 60fps
        for i, id in enumerate(self.subset):
            self.videos.append(cv2.VideoCapture(str(video_files[id])))
            num_frames = int(self.videos[-1].get(cv2.CAP_PROP_FRAME_COUNT))
            self.num_frames = min(num_frames, self.num_frames)

    def __len__(self) -> int:
        return self.num_frames

    def __getitem__(self, index) -> typing.Any:
        masks = []
        for vid in self.videos:
            vid.set(cv2.CAP_PROP_POS_FRAMES, index)
            ok, frame = vid.read()
            masks.append(
                frame[np.newaxis, ..., 0].astype(np.float32) / 255.0
            )
        return {"mask": np.stack(masks)}