from pathlib import Path

from flask import Flask, render_template, request

from .config import Config
from .generator import CyberpunkGenerator, GenerationParams


def create_app() -> Flask:
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    generator = CyberpunkGenerator(model_id=Config.MODEL_ID, output_dir=Config.OUTPUT_DIR)

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @app.route("/generate", methods=["POST"])
    def generate_image():
        prompt = request.form.get("prompt", "").strip()
        negative_prompt = request.form.get("negative_prompt", "").strip()

        steps = int(request.form.get("num_inference_steps", Config.DEFAULT_STEPS))
        guidance = float(request.form.get("guidance_scale", Config.DEFAULT_GUIDANCE))
        height = int(request.form.get("height", Config.DEFAULT_HEIGHT))
        width = int(request.form.get("width", Config.DEFAULT_WIDTH))

        seed_raw = request.form.get("seed", "").strip()
        seed = int(seed_raw) if seed_raw else None

        if not prompt:
            return render_template("index.html", error="Please enter a prompt.")

        params = GenerationParams(
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            guidance_scale=guidance,
            height=height,
            width=width,
            seed=seed,
        )

        output_path = generator.generate(params)
        image_url = f"/{Path(output_path).as_posix()}"

        return render_template(
            "result.html",
            prompt=prompt,
            image_url=image_url,
            params=params,
        )

    return app
