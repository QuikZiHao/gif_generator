from fastapi import APIRouter
from config.entity import VideoSegmentationEntity
from implements.video_segment_impl import video_segment_implment


router = APIRouter()


@router.post("/segment-video")
async def video_segment_service(request: VideoSegmentationEntity):
    """
    Perform video segmentation, mask cropping, and GIF generation.

    Args:
        positive_points (List[List[int]]): Positive points for segmentation.
        negative_points (List[List[int]]): Negative points for segmentation.
        frame_duration (float): Duration of each frame in the final GIF.
    
    Returns:
        str: Success message or raises an exception on failure.
    """
    return await video_segment_implment(
        positive_points=request.positive_points, 
        negative_points=request.negative_points, 
        frame_duration=request.frame_duration
    )

