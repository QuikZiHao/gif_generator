from fastapi.responses import JSONResponse
from ..utils.get_first_frame import get_first_frame


async def get_first_frame_implment():
    try:
        img = get_first_frame()
        return JSONResponse(status_code=200, content={"message": "Get image success!", "image": img})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"An Error occured during getting first frame: {e}"})
