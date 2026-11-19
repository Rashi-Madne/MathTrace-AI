# MathTrace AI

**An AI-assisted mathematics learning prototype for detecting the earliest incorrect step in a student's algebraic solution.**

MathTrace AI analyzes step-by-step algebra solutions, checks consecutive equation transformations, and provides feedback for selected mathematical errors.

Rather than checking only the final answer, the project focuses on examining the intermediate steps where a student's mathematical reasoning may become incorrect.

---

## Problem Statement

Students often make mistakes during intermediate algebraic transformations without realizing where their reasoning became incorrect.

Traditional answer-checking approaches may identify an incorrect final answer but fail to explain the first point at which the solution went wrong.

MathTrace AI explores how symbolic mathematics and rule-based error detection can help identify such mistakes and provide more useful step-level feedback.

## Key Features

- **Typed Equation Input:** Accepts multiple algebraic equations as a student's step-by-step solution.
- **Safe Expression Parsing:** Uses Python's Abstract Syntax Tree (AST) to parse supported mathematical expressions.
- **Symbolic Validation:** Uses SymPy to represent equations and compare their solution sets.
- **First-Error Localization:** Identifies the earliest detected invalid transition in a sequence.
- **Error Classification:** Detects selected sign errors and possible arithmetic errors using rule-based checks.
- **Corrective Feedback:** Generates explanations and corrected equations for supported error patterns.
- **Interactive Interface:** Provides a Streamlit application for entering and evaluating algebraic solutions.

## Example

Consider the following student solution:

**Input**

```text
2*x + 3 = 11
2*x = 8
x = 18
```

**Expected system feedback**

- The first transformation is valid.
- The second transformation contains a possible arithmetic error.
- The detected incorrect step is identified.
- The expected corrected equation is:

```text
x = 4
```

This example demonstrates the project's current arithmetic-error detection capability for a supported pattern.

## How It Works

The current application follows this processing workflow:

1. **Student Input:** The student enters a sequence of typed algebraic equations.
2. **Input Parsing:** The parser validates the input structure and converts supported expressions into SymPy representations.
3. **Mathematical Validation:** Consecutive equations are examined using the current symbolic validation approach.
4. **Error Detection:** Supported rule-based checks examine selected incorrect transformations.
5. **First-Error Localization:** The system identifies the earliest detected invalid transition.
6. **Feedback Generation:** The application displays an explanation and a corrected equation when the implemented checks can provide one.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Core application development |
| SymPy | Symbolic mathematics, equation representation and solution-set comparison |
| Streamlit | Interactive web application |
| pytest | Automated unit and integration testing |
| Git and GitHub | Version control and project hosting |


## Project Structure

```text
MathTrace-AI/
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DEVELOPMENT_LOG.md
│   ├── EXPLANATION_ENGINE_DESIGN.md
│   ├── FEEDBACK_REQUIREMENTS.md
│   ├── REQUIREMENTS.md
│   └── SUPPORTED_TRANSFORMATIONS.md
│
├── src/
│   └── mathtrace/
│       ├── __init__.py
│       ├── parser.py
│       └── validator.py
│
├── tests/
│   ├── test_parser.py
│   └── test_validator.py
│
├── app.py
├── pyproject.toml
├── requirements.txt
├── CHANGELOG.md
├── .gitignore
└── README.md
```

## Installation and Setup

### Prerequisites

- Python 3.12 or a compatible Python installation.
- Git.
- A terminal or command-line interface.

### 1. Clone the Repository

```bash
git clone https://github.com/Rashi-Madne/MathTrace-AI.git
```

Navigate into the project directory:

```bash
cd MathTrace-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

Streamlit will start the application and provide a local URL in the terminal.

## Running Automated Tests

The project uses pytest for automated testing.

Run the complete test suite:

```bash
pytest -v
```


### Latest Verification

| Metric | Result |
|---|---:|
| Automated tests passed | 69 |
| Test execution time | 2.05 seconds |
| Failed tests | 0 |
| Focused regression tests | Passed |

The test suite covers parser functionality, mathematical validation, selected error-detection patterns, invalid input handling, and integration between components.

## Current Implementation Status

**Implemented**

- Python development environment and project packaging.
- Safe typed mathematical expression parsing using AST.
- Equation parsing and multi-step solution processing.
- SymPy-based equation and solution-set comparison.
- Detection of selected sign errors.
- Detection of possible arithmetic errors for supported patterns.
- First-error localization.
- Corrected-equation generation for supported cases.
- Interactive Streamlit application.
- Automated unit and integration tests.

**Future Improvements**

- Broader algebraic transformation support.
- More reliable error classification.
- Expanded mathematical explanations.
- Additional edge-case handling.
- Systematic evaluation using student-style mathematical solutions.

**Not Yet Implemented**

- Handwritten mathematical equation recognition.
- OCR-based solution input.
- Image-based mathematical expression processing.
- General-purpose mathematical error detection.
- Advanced mathematics support.


## Current Limitations

MathTrace AI is an experimental prototype, not a universal mathematical validator.

- Only the variable `x` is currently supported.
- Multiplication must be explicit, for example, `2*x`.
- Error classification uses limited rule-based checks and heuristics.
- The system does not identify every possible mathematical mistake.
- Passing the current validation checks does not guarantee that every individual algebraic operation is mathematically justified.
- Handwriting recognition and OCR are not currently available.

These limitations define the current scope and provide direction for future development.

## Future Scope

- Integrate handwriting recognition and mathematical OCR.
- Convert handwritten solutions into structured mathematical expressions.
- Expand support for algebraic transformations.
- Improve error classification and explanation generation.
- Evaluate the system using a larger collection of student-style mathematical solutions.
- Investigate additional mathematical domains and problem types.

## Documentation

Detailed project documentation is available in the `docs/` directory:

- `REQUIREMENTS.md` — Project requirements and scope.
- `ARCHITECTURE.md` — System architecture and component design.
- `DEVELOPMENT_LOG.md` — Chronological development history.
- `SUPPORTED_TRANSFORMATIONS.md` — Supported mathematical transformations.
- `EXPLANATION_ENGINE_DESIGN.md` — Explanation engine design.
- `FEEDBACK_REQUIREMENTS.md` — Feedback requirements.

## Project Information

**Project:** MathTrace AI

**Category:** Software Development / Symbolic Mathematics / Educational Technology

**Primary Language:** Python

**Current Input Type:** Typed algebraic equations

**Repository:** https://github.com/Rashi-Madne/MathTrace-AI

## License

License selection is pending.