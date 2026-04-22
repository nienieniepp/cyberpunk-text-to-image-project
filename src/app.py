"""Flask routes for the cyberpunk text-to-image demo app."""

from flask import Flask, render_template, request, url_for

from .config import Config
from .generator import CyberpunkGenerator, GenerationParams


def create_app() -> Flask:
    """Create and configure the Flask application instance."""
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    # Keep one generator instance alive for the app process.
    generator = CyberpunkGenerator(model_id=Config.MODEL_ID, output_dir=Config.OUTPUT_DIR)

    @app.route("/", methods=["GET"])
    def index():
        """Render the prompt input form."""
        return render_template("index.html")

    @app.route("/generate", methods=["POST"])
    def generate_image():
        """Generate an image from form input and show result page."""
        prompt = request.form.get("prompt", "").strip()
        if not prompt:
            return render_template("index.html", error="Prompt is required.")

        # Optional controls requested for class demo.
        negative_prompt = request.form.get("negative_prompt", "").strip()
        steps = int(request.form.get("num_inference_steps", Config.DEFAULT_STEPS))
        guidance = float(request.form.get("guidance_scale", Config.DEFAULT_GUIDANCE))
        seed_raw = request.form.get("seed", "").strip()
        seed = int(seed_raw) if seed_raw else None

        params = GenerationParams(
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            guidance_scale=guidance,
            seed=seed,
            height=Config.DEFAULT_HEIGHT,
            width=Config.DEFAULT_WIDTH,
        )

        # Save in static/outputs so the browser can load image directly.
        output_path = generator.generate(params)
        image_url = url_for("static", filename=f"outputs/{output_path.name}")

        return render_template("result.html", prompt=prompt, image_url=image_url, params=params)

    return app
