# Cyberpunk City Text-to-Image Generation using Pretrained Stable Diffusion

A final-year university deep learning project that builds a complete text-to-image system for **cyberpunk city scene generation** using pretrained Stable Diffusion.

This repository includes:
- a **Jupyter notebook prototype** for experimentation,
- a **Flask web app** for interactive demo,
- organized project assets for a 5–6 member team.

---

## 1) Project Description

### Problem Statement
Generating visually coherent cyberpunk city scenes from natural language prompts is a practical use case for modern diffusion models. This project explores prompt-controlled generation, reproducibility (seed control), and quality tuning (guidance scale and inference steps).

### Objectives
- Build an end-to-end text-to-image pipeline with pretrained Stable Diffusion.
- Compare prompt engineering strategies for better visual quality.
- Deliver both a research notebook workflow and a web-based demo.
- Prepare a reproducible, team-friendly repository for a university final project.

### Tech Stack
- Python 3.10+
- PyTorch + Diffusers
- Flask
- Jupyter Notebook

---

## 2) Repository Structure

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   └── TEAM_CONTRIBUTIONS_TEMPLATE.md
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
│   ├── js/
│   │   └── main.js
│   └── outputs/
│       └── .gitkeep
├── templates/
│   ├── index.html
│   └── result.html
├── .gitignore
├── CONTRIBUTING.md
├── requirements.txt
└── run.py
```

---

## 3) Installation and Usage

### Prerequisites
- Python 3.10 or newer
- Recommended: CUDA-capable GPU

### Installation
```bash
git clone <your-repo-url>
cd cyberpunk-text-to-image-project
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run the Flask Demo
```bash
python run.py
```
Open: `http://127.0.0.1:5000`

Generated web-app images are saved in: `static/outputs/`

### Run the Notebook Prototype
```bash
jupyter notebook
```
Open: `notebooks/cyberpunk_stable_diffusion_prototype.ipynb`

---

## 4) Suggested Experiments

Use this section as your final project experiment checklist:

1. **Prompt Detail Ablation**
   - Compare short prompts vs detailed prompts.
   - Evaluate scene complexity, lighting, and realism.

2. **Guidance Scale Sweep**
   - Try values: 5.0, 7.5, 10.0, 12.5.
   - Observe prompt adherence vs artifact risk.

3. **Inference Steps Sweep**
   - Try values: 20, 30, 40, 50.
   - Measure visual quality vs generation time.

4. **Seed Reproducibility Test**
   - Fix prompt/settings and vary seeds.
   - Analyze diversity and consistency.

5. **Negative Prompt Study**
   - Compare outputs with and without negative prompts.
   - Track common artifact reduction.

---

## 5) Team Contribution Section (Template)

For the final report and GitHub submission, copy and fill this template:

| Team Member | Role | Key Contributions | Evidence (Commits/Files) |
|---|---|---|---|
| Member A | Model & Inference |  |  |
| Member B | Backend/Flask |  |  |
| Member C | Frontend/UI |  |  |
| Member D | Experiments/Notebook |  |  |
| Member E | Evaluation/Visualization |  |  |
| Member F (optional) | Documentation/PM |  |  |

A reusable version is also available at `docs/TEAM_CONTRIBUTIONS_TEMPLATE.md`.

---

## 6) Course Deliverables Mapping

- **Literature Review**: diffusion models + text-to-image landscape.
- **Implementation**: notebook + Flask app.
- **Experiments**: prompt engineering and hyperparameter sweeps.
- **Evaluation**: qualitative grid and artifact analysis.
- **Final Demo**: live web generation with curated prompts.

---


## 8) Prompt Dataset for Experiments

CSV files for repeatable prompt studies:
- `data/cyberpunk_experiment_prompts.csv` (50 prompts + default settings)
- `data/negative_prompt_library.csv` (reusable negative prompt presets)

Use `negative_prompt_key` to map experiment rows to a library preset.

---

## 9) Notes

- First generation can be slow due to model download/caching.
- CPU inference works but may be significantly slower.
- For deterministic results, keep all settings + seed fixed.
