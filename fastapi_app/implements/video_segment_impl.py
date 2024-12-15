from constant import SPLIT_OUTPUT
from utils.to_gif import to_gif
from utils.crop_img import crop_mask
from utils.add_label import add_label
from utils.load_model import load_model
from utils.segement import video_segement
from fastapi.responses import JSONResponse
from utils.get_first_frame import get_frame_len


async def video_segment_implment(positive_points, negative_points, frame_duration):
    try:
        predictor = load_model("base_plus")
        inference_state = predictor.init_state(video_path=SPLIT_OUTPUT)
        predictor.reset_state(inference_state)
        predictor = add_label(
            predictor=predictor,
            inference_state=inference_state,
            iter_frame=0,
            # positive_points=[[114,117],[379,141],[263,294],[298,365],[244,463],[380,461]],
            positive_points=positive_points,
            negative_points=negative_points
        )
        video_segements = video_segement(predictor=predictor, inference_state=inference_state)
        frame_len = get_frame_len()
        crop_mask(video_segments=video_segements, frame_len=frame_len)
        to_gif(frame_len=frame_len, frame_duration=frame_duration)
        return JSONResponse(status_code=200, content={"message": "Video segmentation success!"})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"An Error occured during segmenting the video: {e}"})
