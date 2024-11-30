import cv2
import os
from pathlib import Path
from constant import SPLIT_OUTPUT


def split_video(video_path: Path):
# Create the output directory if it doesn't exist
    if not os.path.exists(SPLIT_OUTPUT):
        os.makedirs(SPLIT_OUTPUT)

    # Open the video file using OpenCV
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was successfully opened
    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    # Read the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Loop through all the frames and save them as images
    frame_idx = 0
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If we reached the end of the video, break the loop
        if not ret:
            break

        # Save the frame as an image (you can change the format to .jpg or .png)
        frame_filename = os.path.join(SPLIT_OUTPUT, f"{frame_idx:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        frame_idx += 1

    # Release the video capture object
    cap.release()

    print(f"Frames extracted and saved to {SPLIT_OUTPUT}")