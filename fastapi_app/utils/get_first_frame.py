import os
from PIL import Image
from constant import FIRST_FRAME, SPLIT_OUTPUT
from .base64_encoder import encode_image_to_base64


def get_first_frame():
    first_frame_in_vid = Image.open(FIRST_FRAME)
    return encode_image_to_base64(first_frame_in_vid)


def get_frame_len():
    frame_len = len([f for f in os.listdir(SPLIT_OUTPUT) if os.path.isfile(os.path.join(SPLIT_OUTPUT, f))])-1
    return frame_len
