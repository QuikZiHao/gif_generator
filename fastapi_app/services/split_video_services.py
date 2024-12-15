from fastapi import APIRouter, File, UploadFile, Form
from implements.split_video_impl import split_video_implment


router = APIRouter()


@router.post("/split-video")
async def split_video_service(
    video: UploadFile = File(...), 
    fps: int = Form(...)
):
    """
    Upload a video file and split it into frames based on the specified FPS.
    
    - **video**: UploadFile object representing the video file.
    - **fps**: Frames per second to split the video into.
    
    Returns a confirmation message.
    """
    return await split_video_implment(fps, video)

