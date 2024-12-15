import uvicorn
from fastapi import FastAPI
from .services import split_video_services, get_first_frame_services, crop_img_services


app = FastAPI()


app.include_router(split_video_services.router)
app.include_router(get_first_frame_services.router)
app.include_router(crop_img_services.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8686)
