from sam2.build_sam import build_sam2_video_predictor
from typing import List
import numpy as np

def add_label(predictor:build_sam2_video_predictor,
              inference_state,
              iter_frame:int,
              positive_points:List[List[int]],
              negative_points:List[List[int]]
              ) -> build_sam2_video_predictor:
    points = np.array(positive_points + negative_points, dtype=np.float32)
    labels = np.array([1] * len(positive_points) + [0] * len(negative_points), dtype=np.int32)
    predictor.add_new_points_or_box(
    inference_state=inference_state,
    frame_idx=iter_frame,
    obj_id=1,
    points=points,
    labels=labels,
    )
    return predictor