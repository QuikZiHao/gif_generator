from constant import PNG_OUTPUT_DIR, SPLIT_OUTPUT
from typing import Dict
from PIL import Image
import numpy as np
import os

def crop_mask(video_segments: Dict, frame_len: int):
    # Ensure the PNG output directory exists
    os.makedirs(PNG_OUTPUT_DIR, exist_ok=True)

    # Ensure output directory exists
    if not os.path.exists(PNG_OUTPUT_DIR):
        os.makedirs(PNG_OUTPUT_DIR)


    for out_frame_idx in range(0, frame_len):
        # Load the original image (background)
        img_path = os.path.join(SPLIT_OUTPUT, f"{out_frame_idx:04d}.jpg")
        
        # Check if image exists to prevent errors
        if not os.path.exists(img_path):
            print(f"Skipping frame {out_frame_idx}: Image not found.")
            continue

        img = Image.open(img_path).convert("RGBA")  # Convert to RGBA to handle transparency
        img_np = np.array(img)  # Convert to a NumPy array

        # Create an empty (transparent) 4D numpy array of the same size
        # The shape of img_np is (height, width, 4) because it's RGBA
        empty_array = np.zeros_like(img_np)  # Fully transparent (0s for RGBA)

        # Iterate through the segmented objects in this frame and extract the mask areas
        for _, out_mask in video_segments[out_frame_idx].items():
            # Ensure the mask is a 2D binary array (height x width)
            out_mask = np.squeeze(out_mask)  # Remove unnecessary dimensions
            out_mask = (out_mask * 255).astype(np.uint8)  # Convert to 255 for visibility

            # Create a binary mask (0s and 255s) based on the mask
            mask = Image.fromarray(out_mask)

            # Create a NumPy array from the mask (size should be (height, width))
            mask_np = np.array(mask)

            # Extract the masked region from the original image
            # Using the mask, add the masked region to the empty array (transparency where no mask)
            empty_array[mask_np == 255] = img_np[mask_np == 255]

        # Convert the final result to an image
        result_img = Image.fromarray(empty_array)

        # Prepare the output PNG file path
        png_filename = f"{out_frame_idx:04d}_masked.png"
        png_path = os.path.join(PNG_OUTPUT_DIR, png_filename)

        # Save the final result as a PNG (masked areas only visible)
        result_img.save(png_path)

        print(f"Saved {png_filename} as PNG")