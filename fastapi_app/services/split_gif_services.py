from fastapi import APIRouter, File, UploadFile, Form
from implements.split_gif_impl import split_gif_implment


router = APIRouter()


@router.post("/split-gif")
async def split_gif_service(
    gif: UploadFile = File(...)
):
    """
    Upload a gif file and split it into frames.
    
    - **gif**: UploadFile object representing the gif file.
    
    Returns a confirmation message.
    """
    return await split_gif_implment(gif)

