import os
from PIL import Image
from typing import Dict
from constant import SPLIT_OUTPUT


def video_segement(predictor, inference_state):
    video_segments = {}  # video_segments contains the per-frame segmentation results
    for out_frame_idx, out_obj_ids, out_mask_logits in predictor.propagate_in_video(inference_state):
        video_segments[out_frame_idx] = {
            out_obj_id: (out_mask_logits[i] > 0.0).cpu().numpy()
            for i, out_obj_id in enumerate(out_obj_ids)
        }
    return video_segments


def show_segment(frame_stride: int, frame_len: int, video_segments):
    mask_images = []  # List to store mask images
    for out_frame_idx in range(0, frame_len, frame_stride):
        # Open the frame image
        frame_img = Image.open(os.path.join(SPLIT_OUTPUT, f"{out_frame_idx:04d}.jpg"))
        
        # Ensure the frame has an alpha channel (RGBA)
        if frame_img.mode != 'RGBA':
            frame_img = frame_img.convert('RGBA')
        
        # Loop over the objects in the frame
        for out_obj_id, out_mask in video_segments[out_frame_idx].items():
            # Ensure the mask has the same size as the frame
            mask_resized = out_mask.resize(frame_img.size, Image.Resampling.LANCZOS) if out_mask.size != frame_img.size else out_mask
            
            # Convert the mask to RGBA if it's not already
            if mask_resized.mode != 'RGBA':
                mask_resized = mask_resized.convert('RGBA')
            
            # Create a new image that will hold the mask (combine frame and mask)
            mask_img = Image.alpha_composite(frame_img, mask_resized)
            
            # Add the mask image to the list
            mask_images.append(mask_img)

    return mask_images