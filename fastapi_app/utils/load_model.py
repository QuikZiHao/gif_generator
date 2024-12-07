from sam2.build_sam import build_sam2_video_predictor
from constant import DEVICE, CONFIG_PATH
from utils.load_config import load_config

def load_model(model_size:str):
    config = load_config(CONFIG_PATH, model_size)
    return build_sam2_video_predictor(config.model_cfg, config.sam2_checkpoint, device=DEVICE)