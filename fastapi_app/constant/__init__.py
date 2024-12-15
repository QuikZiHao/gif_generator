import os
import torch
from pathlib import Path
from ..utils.load_config import load_config


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
CONFIG_PATH = Path(r"../config.yaml")

INPUT_VIDEO = os.path.join("temp", "input","input.mp4")
SPLIT_OUTPUT = os.path.join("temp","test")
FIRST_FRAME = os.path.join("temp", "test", "0000.jpg")
PNG_OUTPUT_DIR = os.path.join("temp","mask")
GIF_PATH = os.path.join("temp","gif","output.gif")
INPUT_DIR = os.path.join("temp","input")
INPUT_PATH = os.path.join("temp","input","input.mp4")
