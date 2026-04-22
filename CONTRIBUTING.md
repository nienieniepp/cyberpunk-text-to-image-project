# Contributing Guide

Thanks for contributing to this university project.

## Development Workflow
1. Create a feature branch.
2. Implement changes with clear commits.
3. Run local checks before opening a PR.
4. Open a PR using the provided template.

## Local Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code Standards
- Keep functions small and readable.
- Add docstrings/comments for non-obvious logic.
- Prefer reproducibility (seedable experiments).
- Keep generated artifacts out of git.

## Pull Requests
- Explain motivation and expected outcome.
- Link any related issue.
- Add screenshots for UI updates when possible.
- Include test/check commands in PR description.
