import yaml
from pathlib import Path
from config.entity import SAMConfig


def load_config(pathway:Path, model_key: str = "large"):
    with open(pathway, "r") as file:
        data = yaml.safe_load(file)
    if model_key not in data:
        raise ValueError(f"Model key '{model_key}' not found in config.")
    
    # Load the configuration corresponding to the selected model key
    model_config = data[model_key]
    
    # Return a SAMConfig object using the selected model's configuration
    return SAMConfig(**model_config)
