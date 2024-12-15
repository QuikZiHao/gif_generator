import os
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
from utils.split_video import split_video
from constant import INPUT_PATH, INPUT_DIR


async def split_video_implment(fps: int, video: UploadFile = File(...), ):
    os.makedirs(INPUT_DIR, exist_ok=True)

    with open(INPUT_PATH, "wb") as buffer:
        buffer.write(await video.read())

    try:
        split_video(INPUT_PATH,fps)
        return JSONResponse(status_code=200, content={"message": "Video processed"})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"An Error occured during splitting video: {e}"})

    finally:
        os.remove(INPUT_PATH)
