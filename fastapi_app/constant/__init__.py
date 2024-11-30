import os
import yaml
from pathlib import Path
from utils.load_config import load_config


CONFIG_PATH = Path(r"../config.yaml")
CONFIG = load_config(CONFIG_PATH)

SPLIT_OUTPUT = os.path.join("temp","test")
PNG_OUTPUT_DIR = os.path.join("temp","mask")
GIF_PATH = os.path.join("temp","gif","output.gif")
