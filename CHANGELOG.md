# Changelog

All notable changes to MathTrace AI are documented in this file.

The project is currently in its initial development stage. Changes are recorded under the `Unreleased` section until a formal version is published.

## [Unreleased]

### Project Initialization — 2026-10-30 to 2026-10-31

#### Added

- Initial project workspace and directory structure.
- Python 3.12 virtual environment.
- Initial dependency configuration using `requirements.txt`.
- Installation of SymPy, Streamlit, pytest and Pillow.
- Initial development environment verification.

### Repository and Documentation Setup — 2026-11-01

#### Added

- Initial Git repository with the `main` branch.
- `.gitignore` configuration for local environment files, caches and unnecessary generated files.
- Initial project directory structure and Python package initialization.
- Project requirements documentation.
- Proposed system architecture documentation.
- Development log.
- Initial project README.
- Initial changelog.
- GitHub repository setup and remote configuration.
- Initial Git commit:

  `8bb821c — chore: initialize MathTrace AI project structure`

#### Improved

- Converted `requirements.txt` from UTF-16 to UTF-8 encoding.
- Verified the importability of the primary project dependencies.
- Established the initial scope around typed algebraic input and symbolic validation.

### Initial Equation Validator — 2026-11-02

#### Added

- Initial equation comparison functionality using SymPy.
- Sequential solution-step validation in `src/mathtrace/validator.py`.
- Automated tests for equation comparison, invalid transitions, valid sequences and insufficient input.
- Python project packaging through `pyproject.toml`.
- Editable package installation using `pip install -e .`.

#### Improved

- Updated equation comparison to use SymPy's `solveset()` with an explicit variable and real-number domain.
- Updated sequential validation to pass the selected variable.

#### Testing

- Verified 7 automated tests successfully.

### Boolean Equation Handling — 2026-11-03

#### Added

- `get_solution_set()` to handle SymPy Boolean results and ordinary equations.
- Automated tests for Boolean `True`, Boolean `False` and identity-equation comparison.

#### Improved

- Updated `compare_equations()` to use the new solution-set helper.
- Improved handling of equations that SymPy automatically evaluates to Boolean values.

#### Testing

- Verified 10 automated tests successfully.

### Explanation and Sign-Error Detection — 2026-11-04

#### Added

- Initial explanation engine for valid and invalid algebraic transitions.
- Structured mathematical feedback.
- Initial sign-error classification for supported linear-equation transformations.
- Dynamic corrected-equation generation using SymPy.
- Automated tests for sign errors involving positive and negative constants.

#### Testing

- Verified 15 automated tests successfully.

#### Limitations

- Sign-error detection supports restricted equation patterns.
- Generalized algebraic error classification remains under development.

### Safe Text Parser and Streamlit Prototype — 2026-11-06

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

- Expanded parser, validator and integration test coverage.
- Verified 49 automated tests successfully.

### Arithmetic Error Detection Improvements — 2026-11-17

#### Added

- Regression test for arithmetic-error detection involving a non-unit coefficient.
- Coverage for the example transition:

  - `2*x + 3 = 11`
  - `2*x = 8`
  - `x = 18`

#### Improved

- Refined arithmetic-error detection to reduce incorrect classifications.
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

### Parser Robustness and Domain Validation — 2026-11-18

#### Improved

- Strengthened AST-based mathematical expression parsing.
- Improved handling of invalid mathematical operations.
- Added safeguards against division by zero.
- Added safeguards against zero raised to a negative power.
- Improved handling of denominator restrictions and domain-sensitive expressions.
- Strengthened solution-set validation for supported domain restrictions.

#### Testing

- Expanded regression coverage for parser and domain-validation behaviour.
- Verified the complete automated test suite: **69 tests passed**.

### Algebraic Error Detection and Validation — 2026-11-18

#### Improved

- Refined sign-error detection for supported linear-equation transformations.
- Improved handling of non-unit variable coefficients.
- Extended supported sign-error cases involving isolated variables.
- Refined arithmetic-error detection involving coefficients and constants.
- Improved corrected-equation generation for supported error patterns.
- Added safeguards against selected incorrect error classifications.

#### Testing

- Expanded validator regression tests.
- Verified supported sign-error and arithmetic-error scenarios.
- Verified the complete automated test suite: **69 tests passed, 0 failures**.

### Streamlit Interface Refinement — 2026-11-18

#### Improved

- Refined application typography.
- Introduced Poppins for headings and prominent interface text.
- Introduced Inter for general interface text.
- Introduced JetBrains Mono for mathematical expressions and code-like content.
- Preserved the existing application workflow and validation functionality.

### Version Control and Repository Updates — 2026-11-18

#### Changed

- Committed parser and domain-validation improvements:

  `319eab1 — fix: strengthen equation parsing and domain validation`

- Committed algebraic error-detection improvements and regression tests:

  `df4839c — feat: improve algebra error detection and corrections`

- Committed interface typography refinements:

  `7479b9f — style: refine MathTrace interface typography`

#### Verification

- Complete automated test suite: **69 passed, 0 failed**.
- `git diff --check` completed without whitespace errors after cleanup.
- Successfully pushed all three commits to GitHub.
- Confirmed that local `main` and remote `origin/main` point to commit `7479b9f`.
- Temporary untracked files were excluded from the commits.

### Evaluation Dataset and Automated Evaluation — 2026-11-19

#### Added

- Created an initial manually labelled evaluation dataset in `evaluation/evaluation_cases.csv`.
- Added 20 algebra solution cases across four categories:
  - 5 correct solutions.
  - 5 sign-error cases.
  - 5 arithmetic-error cases.
  - 5 other incorrect transformation cases.
- Implemented `evaluation/run_evaluation.py` to automate comparison between expected and actual validator outputs.
- Added evaluation checks for solution status, first detected error step and error category.

#### Testing

- Individually verified all 20 evaluation cases against the existing validator.
- Successfully executed the automated evaluation script using:

  `python -m evaluation.run_evaluation`

- Initial evaluation results:
  - Total cases: 20.
  - Passed: 20.
  - Failed: 0.
  - Observed agreement: 100%.

#### Notes

- The initial evaluation dataset is manually designed and intended for preliminary validation of supported functionality.
- The observed agreement applies only to these 20 evaluation cases and does not establish general mathematical accuracy.
- Individual evaluation-result CSV generation, dataset expansion and detailed performance analysis remain pending.

### Parser and Validator Robustness Improvements — 2026-11-21

#### Added

- Added regression tests for expressions containing up to 100 terms.
- Added tests for positive terms, alternating signs, and combined variable and constant terms.
- Added validator tests for equations with large coefficients.
- Added coverage for detecting and correcting a tested arithmetic error involving large coefficients.

#### Improved

- Strengthened automated test coverage for large algebraic expressions.
- Verified exact rational arithmetic for integer fractions.
- Tested nested expressions, polynomial transformations and selected fractional solutions.

#### Testing

- Complete automated test suite: **76 passed**.
- Parser tests: 46 passed.
- Validator tests: 30 passed.
- Verified valid and invalid large-coefficient equations.
- Confirmed that the Streamlit application launches locally and its homepage loads successfully.

#### Repository

- Added and pushed commit:

  `c178b04 — test: cover large algebraic expressions`

### Streamlit Community Cloud Deployment — 2026-11-21

#### Added

- Deployed MathTrace AI to Streamlit Community Cloud.
- Configured deployment using the GitHub repository.
- Configured `app.py` as the application entry point.
- Successfully launched the application using Python 3.14.

#### Verification

- Confirmed that the deployed Streamlit application starts successfully.
- Confirmed that the application interface loads on the cloud deployment.

#### Notes

- Published as an initial research prototype.
- The deployed application currently supports typed algebraic solution-step validation.
- Generalized equation solving, handwritten equation recognition and broader mathematical error classification remain under development.

---

## Current Implementation Status

| Feature | Status |
|---|---|
| Typed algebra solution input | Implemented |
| Safe AST-based expression parsing | Implemented |
| Division-by-zero safeguards | Implemented |
| Invalid negative-power safeguards | Implemented |
| Domain restriction handling for supported expressions | Implemented |
| Sequential solution-step validation | Implemented |
| First detected invalid transition identification | Implemented |
| Supported sign-error feedback | Implemented |
| Heuristic arithmetic-error feedback | Implemented |
| Corrected-equation generation for supported cases | Implemented |
| Streamlit application interface | Implemented |
| Refined application typography | Implemented |
| Streamlit Community Cloud deployment | Deployed |
| Automated regression test suite | 76 tests passing |
| Handwritten equation recognition (OCR) | Not implemented |
| Generalized algebraic error classification | Not implemented |
| Standalone equation solving with detailed solution generation | Under development |

## Notes

- This changelog records development-stage changes, not formal software releases.
- Error detection is currently limited to selected linear-equation patterns and supported mathematical cases.
- The validator uses symbolic mathematics and rule-based checks; it is not a trained machine-learning model.
- Passing automated tests does not establish universal mathematical correctness.
- OCR, broader mathematical transformation coverage and expanded systematic evaluation remain under development.
- Future changes will be documented under the `Unreleased` section until a formal version is published.