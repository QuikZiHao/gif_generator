import cv2
from constant import INPUT_VIDEO


def drop_frame(fps: int):
    # Open the input video
    cap = cv2.VideoCapture(INPUT_VIDEO)

    # Get original video properties
    original_fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 output

    # Create the VideoWriter object with the desired FPS
    out = cv2.VideoWriter(INPUT_VIDEO, fourcc, fps, (frame_width, frame_height))

    # Frame skipping factor
    frame_skip = max(1, int(original_fps / fps))

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Write only every `frame_skip`th frame
        if frame_count % frame_skip == 0:
            out.write(frame)
        frame_count += 1

    # Release resources
    cap.release()
    out.release()
    print(f"Video frame rate changed to {fps} fps and saved at {INPUT_VIDEO}")
