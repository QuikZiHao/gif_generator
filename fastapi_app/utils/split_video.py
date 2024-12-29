import os
import cv2
import shutil
from pathlib import Path
from utils.drop_frame import drop_frame
from constant import SPLIT_OUTPUT, INPUT_VIDEO


def split_video(fps: int):
    if os.path.exists(SPLIT_OUTPUT):
    # Delete the directory and all its contents
        shutil.rmtree(SPLIT_OUTPUT)
    os.makedirs(SPLIT_OUTPUT)
    # drop_frame(video_path=video_path,fps=fps)
    drop_frame(fps)
    cap = cv2.VideoCapture(INPUT_VIDEO)

    # Check if the video file was successfully opened
    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

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