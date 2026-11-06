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

### Validator Improvement — 2026-11-02

- Updated equation comparison to use SymPy's `solveset()` with an explicit variable and real-number domain.
- Updated sequential solution validation to pass the selected variable.
- Updated the existing automated tests to match the revised function signatures.
- Verified the test suite successfully: **7 tests passed**.
- Investigated SymPy's automatic Boolean evaluation and special equation solution sets.


### Validator Boolean Handling — 2026-11-03

- Added `get_solution_set()` to handle SymPy Boolean results and ordinary equations.
- Updated `compare_equations()` to use the new solution-set helper.
- Added automated tests for Boolean `True`, Boolean `False`, and identity-equation comparison.
- Verified the complete test suite successfully: **10 tests passed**.


### Added
- Initial explanation engine for valid and invalid algebraic transitions.
- Structured mathematical feedback output.
- Tests for explanation engine behavior.

### Limitations
- Specific error classification and correction suggestions are not yet implemented.


### Added
- Initial sign-error classification for supported linear equation transformations.
- Integration of error classification into the explanation engine.
- Dynamic corrected-equation generation using SymPy.
- Automated tests covering sign errors with positive and negative constants.

### Testing
- 15 automated tests passing.

### Limitations
- Sign-error detection currently supports a restricted equation pattern.
- Generalized algebraic error classification remains under development.


### Added
- Safe AST-based parsing of mathematical expressions.
- Parsing of complete equations and multiple solution steps.
- Text-based integration with the symbolic equation validator.
- Controlled invalid-input responses for malformed equations.

### Improved
- Cleaned up unreachable duplicate logic in sign-error detection.
- Expanded automated tests for parser and validator integration.

### Added
- Safe parsing of mathematical expressions and equations.
- Multi-step algebra solution validation.
- Text-based solution input validation.
- Initial Streamlit interface for checking algebra solution steps.
- Feedback for supported sign errors and possible arithmetic errors.

### Improved
- First-invalid-step identification in multi-step solutions.
- Structured handling of malformed and unsupported mathematical input.

### Testing
- Added parser and integration test coverage.
- Verified 49 automated tests successfully.