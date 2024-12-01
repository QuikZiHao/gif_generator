import os
import yaml
from pathlib import Path
import torch
from utils.load_config import load_config


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
CONFIG_PATH = Path(r"../config.yaml")


SPLIT_OUTPUT = os.path.join("temp","test")
PNG_OUTPUT_DIR = os.path.join("temp","mask")
GIF_PATH = os.path.join("temp","gif","output.gif")
INPUT_PATH = os.path.join("temp","input","input.mp4")
