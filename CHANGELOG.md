# Changelog

All notable changes to MathTrace AI are documented in this file.

The project is currently in its initial development stage. Changes are recorded under the `Unreleased` section until a formal version is published.

## [Unreleased]

### Development Milestone — 2026-11-01

#### Added
- Initial project workspace and Python virtual environment.
- Dependency configuration using `requirements.txt`.
- Git repository initialization with the `main` branch.
- `.gitignore` configuration for local environment files, caches, and sensitive files.
- Initial project directory structure and Python package initialization.
- Project requirements, proposed architecture, and development log documentation.
- Initial project README.
- Verification of primary Python library imports.

### Validator Implementation — 2026-11-02

#### Added
- Initial equation comparison functionality using SymPy.
- Sequential solution-step validation in `src/mathtrace/validator.py`.
- Automated tests for equation comparison, invalid transitions, valid sequences, and insufficient input.

#### Improved
- Updated equation comparison to use SymPy's `solveset()` with an explicit variable and real-number domain.
- Updated sequential validation to pass the selected variable.

#### Testing
- Verified 7 automated tests successfully.

### Boolean Handling — 2026-11-03

#### Added
- `get_solution_set()` to handle SymPy Boolean results and ordinary equations.
- Automated tests for Boolean `True`, Boolean `False`, and identity-equation comparison.

#### Improved
- Updated `compare_equations()` to use the new solution-set helper.

#### Testing
- Verified 10 automated tests successfully.

### Explanation and Sign-Error Detection — 2026-11-04

#### Added
- Initial explanation engine for valid and invalid algebraic transitions.
- Structured mathematical feedback.
- Initial sign-error classification for supported linear equation transformations.
- Dynamic corrected-equation generation using SymPy.
- Automated tests for sign errors involving positive and negative constants.

#### Testing
- Verified 15 automated tests successfully.

#### Limitations
- Sign-error detection supports restricted equation patterns.
- Generalized algebraic error classification remains under development.

### Text Parser and Streamlit Prototype — 2026-11-06

#### Added
- Safe AST-based parsing of mathematical expressions and equations.
- Parsing of complete equations and multiple solution steps.
- Text-based integration with the symbolic equation validator.
- Controlled invalid-input responses for malformed equations.
- Initial Streamlit interface for checking algebra solution steps.
- Feedback for supported sign errors and possible arithmetic errors.

#### Improved
- First-invalid-step identification in multi-step solutions.
- Structured handling of malformed and unsupported mathematical input.
- Removed unreachable duplicate logic in sign-error detection.

#### Testing
- Expanded parser, validator, and integration test coverage.
- Verified 49 automated tests successfully.

### Arithmetic Error Detection Improvements — 2026-11-17

#### Added
- Regression test for arithmetic error detection involving a non-unit coefficient.
- Coverage for the example transition:
  - `2*x + 3 = 11`
  - `2*x = 8`
  - `x = 18`

#### Improved
- Refined arithmetic error detection to reduce incorrect classifications.
- Added safeguards for transformations involving non-unit coefficients and nonzero constants.
- Improved corrected-equation calculation using the original equation's coefficient and constant.
- Improved feedback for supported arithmetic errors.

#### Testing
- Verified the complete automated test suite: **50 tests passed**.
- Confirmed the regression test detects the incorrect final step and produces the expected correction: `x = 4`.

### Documentation Improvements — 2026-11-17

#### Updated
- Reworked the README to reflect the current implementation and setup instructions.
- Updated architecture documentation to describe implemented components.
- Revised explanation engine design and supported transformation documentation.
- Clarified current feedback requirements and functional requirements.
- Documented implementation limitations and future development scope.

---

## Current Implementation Status

- Typed algebra solution input: Implemented.
- Safe expression and equation parsing: Implemented.
- Sequential solution-step validation: Implemented.
- First detected invalid transition identification: Implemented.
- Supported sign-error feedback: Implemented.
- Heuristic possible arithmetic-error feedback: Implemented.
- Streamlit prototype: Implemented.
- Automated test suite: 59 tests passing.
- Handwritten equation recognition (OCR): Not implemented.
- Generalized algebraic error classification: Not implemented.

## Notes

- This changelog records development-stage changes, not formal software releases.
- Error detection is currently limited to selected linear-equation patterns.
- Passing automated tests does not establish universal mathematical error-detection accuracy.
- Future changes will be documented here as development progresses.