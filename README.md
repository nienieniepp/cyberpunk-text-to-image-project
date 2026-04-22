# Cyberpunk City Text-to-Image Generation using Pretrained Stable Diffusion

A university deep learning course project repository that demonstrates text-to-image generation for cyberpunk city scenes using a pretrained Stable Diffusion model.

## Team Scope (5–6 Members)

This repository is designed for team-based development with clear modular ownership:

- **Model & Inference Lead**: `src/generator.py`
- **Backend/API Lead**: `src/app.py`
- **Frontend/UI Lead**: `templates/`, `static/`
- **Experimentation Lead**: `notebooks/`
- **MLOps/DevOps Lead**: environment setup, reproducibility, deployment
- **Documentation/QA Lead**: testing plan, reports, presentation assets

## Repository Structure

```text
.
├── notebooks/
│   └── cyberpunk_stable_diffusion_prototype.ipynb
├── outputs/
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── generator.py
│   └── utils.py
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── main.js
├── templates/
│   ├── index.html
│   └── result.html
├── .gitignore
├── requirements.txt
└── run.py
```

## Features

- Stable Diffusion text-to-image pipeline integration via `diffusers`
- Flask web app for prompt-driven generation
- Configurable generation parameters (steps, guidance scale, resolution, seed)
- Deterministic generation support through seed control
- Notebook prototype for fast experimentation and reporting
- Organized outputs in `/outputs`

## Setup

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Flask App

```bash
python run.py
```

Then open: `http://127.0.0.1:5000`

## Notebook Prototype

Open and run:

- `notebooks/cyberpunk_stable_diffusion_prototype.ipynb`

## Recommended Hardware

- GPU with CUDA support (recommended for practical generation speed)
- CPU mode is available but significantly slower

## Course Deliverables Mapping

- **Proposal & Literature Review**: model choice and cyberpunk prompt engineering strategy
- **Implementation**: notebook prototype + Flask application
- **Experiments**: prompt variants, seed control, hyperparameter sweeps
- **Evaluation**: qualitative analysis and curated output gallery
- **Final Demo**: interactive web generation + report slides

## Notes

- First model load may take time and disk space.
- Generated images are saved to `outputs/`.
