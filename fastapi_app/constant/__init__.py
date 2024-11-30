import yaml
from pathlib import Path
from utils.load_config import load_config


CONFIG_PATH = Path(r"../config.yaml")
CONFIG = load_config(CONFIG_PATH)