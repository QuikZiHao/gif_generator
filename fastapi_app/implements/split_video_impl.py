import os
from fastapi import FastAPI, File, UploadFile
from constant import INPUT_PATH
from fastapi.responses import JSONResponse
from utils.split_video import split_video

async def split_video_implment(video: UploadFile = File(...), fps: int):
    with open(INPUT_PATH, "wb") as buffer:
        buffer.write(await video.read())

    try:
        # Call the service function to split the video
        split_video(INPUT_PATH,fps)

        # Return the list of saved frames or the result
        return JSONResponse(content={"message": "Video processed"})

    finally:
        # Clean up: remove the temporarily saved video
        os.remove(INPUT_PATH)
