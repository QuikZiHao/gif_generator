from constant import SPLIT_OUTPUT
import os
from PIL import Image

def video_segement(predictor, inference_state):
    video_segments = {}  # video_segments contains the per-frame segmentation results
    for out_frame_idx, out_obj_ids, out_mask_logits in predictor.propagate_in_video(inference_state):
        video_segments[out_frame_idx] = {
            out_obj_id: (out_mask_logits[i] > 0.0).cpu().numpy()
            for i, out_obj_id in enumerate(out_obj_ids)
        }
    return video_segments

def show_segement(frame_stride:int, frame_len:int, video_segments):
    mask_images = []  # List to store mask images
    for out_frame_idx in range(0, frame_len, frame_stride):
        # Open the frame image
        frame_img = Image.open(os.path.join(SPLIT_OUTPUT, f"{out_frame_idx:04d}.jpg"))
        
        # Loop over the objects in the frame
        for out_obj_id, out_mask in video_segments[out_frame_idx].items():
            # Create a new image that will hold the mask
            mask_img = frame_img.copy()
            mask_img.paste(out_mask, (0, 0), out_mask)  # Use the mask for transparency (alpha)
            
            # Add the mask image to the list
            mask_images.append(mask_img)

    return mask_images

