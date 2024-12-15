import os
import cv2
import imageio
import numpy as np
from constant import PNG_OUTPUT_DIR, GIF_PATH


def to_gif(frame_len: int, frame_duration: float):
    # List to store all frames
    frames = []

    # Iterate through the expanded images
    for i in range(frame_len):
        # Read each expanded image
        img = cv2.imread(f'{PNG_OUTPUT_DIR}/{i:04d}_masked.png', cv2.IMREAD_UNCHANGED)

        # Ensure the image is loaded correctly
        if img is not None:
            # Since the GIF size equals the image size, no need to calculate offsets or use a canvas
            img_rgba = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)

            # # Replace transparent pixels with a white background
            # h, w, _ = img_rgba.shape
            # white_bg = np.full((h, w, 3), (255, 255, 255), dtype=np.uint8)  # White canvas

            # # Create a mask for transparency (alpha = 0)
            # alpha_channel = img_rgba[:, :, 3]
            # mask = alpha_channel == 0  # Fully transparent pixels

            # # Combine the image with the white background
            # img_rgb = img_rgba[:, :, :3]  # Drop alpha channel
            # img_rgb[mask] = white_bg[mask]  # Replace transparent pixels with white

            # Append to frames
            frames.append(img_rgba)

    gif_dir = os.path.dirname(GIF_PATH)
    os.makedirs(gif_dir, exist_ok=True)

    # Save all frames as a GIF
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
