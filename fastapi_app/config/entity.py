from typing import List
from pydantic import BaseModel
from dataclasses import dataclass


@dataclass
class SAMConfig:
    sam2_checkpoint: str 
    model_cfg: str 

class VideoSegmentationEntity(BaseModel):
    positive_points: List[List[int]]
    negative_points: List[List[int]] = []
    frame_duration: float = 0.01