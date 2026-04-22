"""Model inference utilities for Stable Diffusion image generation."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import torch
from PIL import Image, ImageDraw

from .config import Config
from .utils import build_output_filename, ensure_output_dir

try:
    from diffusers import StableDiffusionPipeline
except Exception:  # pragma: no cover
    # Fallback mode keeps the demo app importable in restricted environments.
    StableDiffusionPipeline = None


@dataclass
class GenerationParams:
    """Container for user-selected generation settings."""

    prompt: str
    negative_prompt: str = ""
    num_inference_steps: int = Config.DEFAULT_STEPS
    guidance_scale: float = Config.DEFAULT_GUIDANCE
    height: int = Config.DEFAULT_HEIGHT
    width: int = Config.DEFAULT_WIDTH
    seed: Optional[int] = None


class CyberpunkGenerator:
    """Lazy-loading generator wrapper around diffusers pipeline."""

    def __init__(self, model_id: str = Config.MODEL_ID, output_dir: str = Config.OUTPUT_DIR):
        self.model_id = model_id
        self.output_dir = ensure_output_dir(output_dir)
        self.device = "cuda" if (Config.DEVICE == "cuda" and torch.cuda.is_available()) else "cpu"
        self.pipeline = None

    def _load_pipeline(self):
        """Load model once per process for faster subsequent generations."""
        if self.pipeline is not None:
            return

        if StableDiffusionPipeline is None:
            self.pipeline = "mock"
            return

        dtype = torch.float16 if self.device == "cuda" else torch.float32
        self.pipeline = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=dtype)
        self.pipeline = self.pipeline.to(self.device)

    def generate(self, params: GenerationParams) -> Path:
        """Generate an image from params and return the saved file path."""
        self._load_pipeline()

        # Manual seed enables reproducible runs for experiments.
        generator = None
        if params.seed is not None:
            generator = torch.Generator(device=self.device).manual_seed(params.seed)

        output_path = self.output_dir / build_output_filename("cyberpunk_city")

        if self.pipeline == "mock":
            image = self._mock_image(params.prompt, params.width, params.height)
        else:
            result = self.pipeline(
                prompt=params.prompt,
                negative_prompt=params.negative_prompt,
                num_inference_steps=params.num_inference_steps,
                guidance_scale=params.guidance_scale,
                height=params.height,
                width=params.width,
                generator=generator,
            )
            image = result.images[0]

        image.save(output_path)
        return output_path

    @staticmethod
    def _mock_image(prompt: str, width: int, height: int) -> Image.Image:
        """Simple placeholder image used when diffusion dependencies are unavailable."""
        image = Image.new("RGB", (width, height), color=(22, 24, 45))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, height - 70, width, height), fill=(117, 0, 178))
        draw.text((20, 20), "Mock Generation Mode", fill=(0, 255, 255))
        draw.text((20, 48), f"Prompt: {prompt[:60]}", fill=(240, 240, 240))
        return image
