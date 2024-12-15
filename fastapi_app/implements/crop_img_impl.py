from fastapi.responses import JSONResponse
from utils.get_first_frame import get_frame_len
from utils.crop_img import crop_image, resize_image


async def crop_img_implement(crop_box: list):
    try:
        frame_len = get_frame_len()
        crop_image(crop_box, frame_len)
        return JSONResponse(status_code=200, content={"message": "Crop image done."})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error occured while cropping image: {e}"})


async def resize_img_implement(height: int, width: int):
    try:
        frame_len = get_frame_len()
        resize_image(height, width, frame_len)
        return JSONResponse(status_code=200, content={"message": "Resize image done."})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Error occured while resizing image: {e}"})