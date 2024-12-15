from typing import List
from fastapi import APIRouter, Form, HTTPException
from implements.crop_img_impl import crop_img_implement, resize_img_implement


router = APIRouter()


@router.post("/crop-img")
async def crop_image_service(
    x1: int = Form(..., description="x1 coordinate"),
    y1: int = Form(..., description="y1 coordinate"),
    x2: int = Form(..., description="x2 coordinate"),
    y2: int = Form(..., description="y2 coordinate"),
):
    """
    Crop an image using the specified crop box.

    - **crop_box**: List of 4 integers representing [x1, y1, x2, y2].
    
    Returns a success or failure message.
    """
    crop_box: List[int] = [x1, y1, x2, y2]
    if len(crop_box) != 4:
        raise HTTPException(status_code=400, detail="Crop box must contain exactly 4 integers.")
    return await crop_img_implement(crop_box)


@router.post("/resize-img")
async def resize_image_service(
    height: int = Form(512),
    width: int = Form(512)
):
    """
    Resize an image to the specified height and width.

    - **height**: Desired height of the resized image.
    - **width**: Desired width of the resized image.

    Returns a success or failure message.
    """
    return await resize_img_implement(height, width)
