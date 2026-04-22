import os


class Config:
    MODEL_ID = os.getenv("MODEL_ID", "runwayml/stable-diffusion-v1-5")
    OUTPUT_DIR = os.getenv("OUTPUT_DIR", "outputs")
    DEVICE = os.getenv("DEVICE", "cuda")
    DEFAULT_HEIGHT = int(os.getenv("DEFAULT_HEIGHT", 512))
    DEFAULT_WIDTH = int(os.getenv("DEFAULT_WIDTH", 512))
    DEFAULT_STEPS = int(os.getenv("DEFAULT_STEPS", 30))
    DEFAULT_GUIDANCE = float(os.getenv("DEFAULT_GUIDANCE", 7.5))
