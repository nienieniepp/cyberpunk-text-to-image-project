from datetime import datetime
from pathlib import Path


def ensure_output_dir(path: str) -> Path:
    output_path = Path(path)
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def build_output_filename(prefix: str = "cyberpunk") -> str:
    stamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S_%f")
    return f"{prefix}_{stamp}.png"
