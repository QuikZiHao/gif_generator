from fastapi import APIRouter
from ..implements.get_first_frame_impl import get_first_frame_implment


router = APIRouter()


@router.post("/get-first-frame")
async def get_first_frame_service():
    return await get_first_frame_implment()
