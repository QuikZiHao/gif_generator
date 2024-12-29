import os
from PIL import Image
import shutil
from constant import SPLIT_OUTPUT, INPUT_GIF

def split_gif():
    # Create the output directory if it doesn't exist
    if os.path.exists(SPLIT_OUTPUT):
    # Delete the directory and all its contents
        shutil.rmtree(SPLIT_OUTPUT)

    # Create the directory again
    os.makedirs(SPLIT_OUTPUT)


    # Open the GIF file using Pillow
    try:
        with Image.open(INPUT_GIF) as gif:
            frame_idx = 0

            while True:
                # Save the current frame as an image (you can change the format to .jpg or .png)
                frame_filename = os.path.join(SPLIT_OUTPUT, f"{frame_idx:04d}.jpg")
                gif.save(frame_filename, format="PNG")

                frame_idx += 1

                # Attempt to move to the next frame
                try:
                    gif.seek(frame_idx)
                except EOFError:
                    # Break if no more frames are available
                    break

        print(f"Frames extracted and saved to {SPLIT_OUTPUT}")

    except FileNotFoundError:
        print(f"Error: File {INPUT_GIF} not found.")
        exit()
    except Exception as e:
        print(f"Error: {e}")
        exit()
