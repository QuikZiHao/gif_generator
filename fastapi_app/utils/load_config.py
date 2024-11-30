import yaml
from pathlib import Path
from config.entity import SAMConfig


def load_config(pathway:Path):
    with open(pathway, "r") as file:
        data = yaml.safe_load(file)
    return SAMConfig(**data)
