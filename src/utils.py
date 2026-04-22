"""Filesystem helper functions for output management."""

from datetime import datetime
from pathlib import Path


def ensure_output_dir(path: str) -> Path:
    """Create output directory if it doesn't exist and return Path."""
    output_path = Path(path)
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def build_output_filename(prefix: str = "cyberpunk") -> str:
    """Generate a timestamped output filename for unique image saves."""
    stamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S_%f")
    return f"{prefix}_{stamp}.png"
