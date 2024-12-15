import os
import cv2
import numpy as np
from typing import Dict
from constant import SPLIT_OUTPUT


def merge_mask(segements: Dict[int, np.ndarray]):
    mask = np.zeros_like(next(iter(segements.values())), dtype=np.uint8)
    for segement in segements.values():
        mask = np.logical_or(mask, segement).astype(np.uint8)

    return mask


def apply_mask(ori_mask:np.ndarray, image: np.ndarray) -> np.ndarray:
    if image is None:
        print("Error: Unable to load image.")
    else:
        print("Image loaded successfully. Shape:", image.shape)
    # Ensure the mask is scaled properly to 255
    mask = (ori_mask[0] * 255).astype(np.uint8)
    height, width, _ = image.shape
    
    # Create the red color mask (R=255, G=0, B=0)
    red_mask = np.zeros((height, width, 3), dtype=np.uint8)
    red_mask[:, :, 2] = mask  # Set the red channel intensity based on the mask
    
    # Overlay the red mask onto the original image
    overlayed_image = cv2.addWeighted(image, 1.0, red_mask, 0.8, 0)
    
    return overlayed_image


def show_mask(frame_stride:int, video_segements: Dict[int, Dict[int, np.ndarray]]):
    mask_list = []
    for frame in range(0,len(video_segements),frame_stride):
        image_path = os.path.join(SPLIT_OUTPUT,f"{frame:04d}.jpg")
        image = cv2.imread(image_path)
        mask = merge_mask(video_segements[frame])
        result = apply_mask(mask,image)
        mask_list.append(result)
    return mask_list



    