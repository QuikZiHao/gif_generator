import cv2
import imageio
import numpy as np
from ..constant import PNG_OUTPUT_DIR, GIF_PATH


def to_gif(frame_len:int, frame_duration:float):
    # List to store all frames
    frames = []

    # Iterate through the expanded images
    for i in range(frame_len):
        # Read each expanded image
        img = cv2.imread(f'{PNG_OUTPUT_DIR}/{i:04d}_masked.png', cv2.IMREAD_UNCHANGED)

        # Ensure the image is loaded correctly
        if img is not None:
    # Since the GIF size equals the image size, no need to calculate offsets or use a canvas
            img_rgba = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)  # Convert directly to RGBA
            
            # Append the image to the frames list
            frames.append(img_rgba)

    # Save all frames as a GIF with frame disposal method 2 (clear previous frame)
    imageio.mimsave(
        GIF_PATH,
        frames,
        format='GIF',
        duration=frame_duration,  # Frame duration (seconds)
        loop=0,        # Loop forever
        transparency=0,  # Set transparency to 0 (transparent background)
        disposal=2      # Disposal method 2: clear previous frame before displaying the next
    )

    print(f"GIF saved as '{GIF_PATH}'")
