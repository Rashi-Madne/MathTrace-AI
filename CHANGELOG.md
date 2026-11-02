# Changelog

All notable changes to MathTrace AI will be documented in this file.

The project currently follows an initial development-stage versioning approach.

## [Unreleased]

### Development Milestone — 2026-11-01

### Added
- Initial project workspace and Python virtual environment.
- Dependency configuration using `requirements.txt`.
- Git repository initialization with the `main` branch.
- `.gitignore` configuration for local environment files, caches, and secrets.
- Initial project directory structure.
- Python package initialization file.
- Project requirements documentation.
- Proposed system architecture documentation.
- Development log.
- Initial project README.
- Verification of the primary Python library imports.

### Project Status
- Core mathematical reasoning engine: Not implemented.
- Earliest-error detection: Not implemented.
- Explanation generation: Not implemented.
- Streamlit interface: Not implemented.
- Automated application tests: Not implemented.

### Development Milestone — 2026-11-02

- Added `pyproject.toml` with project metadata, dependencies, package discovery, and pytest configuration.
- Installed MathTrace AI in editable mode.
- Implemented initial equation comparison and sequential solution-step validation in `src/mathtrace/validator.py`.
- Added automated tests covering equation comparison, invalid transitions, valid sequences, and insufficient input.
- Verified the initial test suite: **7 tests passed**.