from dataclasses import dataclass


@dataclass
class SAMConfig:
    sam2_checkpoint: str 
    model_cfg: str 