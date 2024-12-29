import os
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
from utils.split_gif import split_gif
from constant import INPUT_GIF, INPUT_DIR


async def split_gif_implment(gif: UploadFile = File(...), ):
    os.makedirs(INPUT_DIR, exist_ok=True)

    with open(INPUT_GIF, "wb") as buffer:
        buffer.write(await gif.read())

    try:
        split_gif()
        return JSONResponse(status_code=200, content={"message": "gif processed"})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"An Error occured during splitting gif: {e}"})

    finally:
        os.remove(INPUT_GIF)
