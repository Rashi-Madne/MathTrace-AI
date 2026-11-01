# MathTrace AI

An intelligent mathematics learning assistant for identifying the earliest incorrect step in a student's algebraic solution.

## Overview

MathTrace AI is a mathematics learning assistant designed to analyze step-by-step algebraic solutions, identify the earliest incorrect mathematical transformation, and explain why the mistake occurred.

Instead of checking only the final answer, the system aims to evaluate the reasoning between consecutive solution steps and provide mathematically justified feedback.

## Problem Statement

Students can make mistakes during intermediate algebraic transformations without realizing where their reasoning became incorrect. Traditional answer-checking approaches may identify an incorrect final answer but fail to explain the first point at which the solution went wrong.

MathTrace AI aims to address this problem through symbolic mathematical verification and step-level error detection.

## Key Objectives

- Analyze student-submitted algebraic solution steps.
- Verify supported mathematical transformations.
- Identify the earliest detected incorrect step.
- Explain mathematical errors in understandable language.
- Suggest a justified correction when possible.

## Proposed Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Core development |
| SymPy | Symbolic mathematics |
| Streamlit | User interface |
| pytest | Automated testing |
| Pillow | Image processing foundation |
| Git and GitHub | Version control |

## Proposed Architecture

1. Student input
2. Input processing and validation
3. Symbolic mathematical reasoning
4. Earliest-error detection
5. Explanation generation
6. Student feedback

## Initial Scope and Limitations

The initial prototype will focus on typed algebraic expressions and a defined subset of algebraic transformations.

The system will prioritize symbolic verification and rule-based explanations. It will distinguish between verified errors, valid transformations, and cases that cannot be reliably evaluated.

Handwritten input, image-based processing, and advanced mathematical topics are outside the initial implementation scope.

## Project Structure

```text
MathTrace-AI/
├── docs/
│   ├── DEVELOPMENT_LOG.md
│   ├── REQUIREMENTS.md
│   └── ARCHITECTURE.md
├── src/
│   └── mathtrace/
│       └── __init__.py
├── tests/
├── .gitignore
├── requirements.txt
├── README.md
└── CHANGELOG.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd MathTrace-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Project Status

**Current phase:** Project initialization and technical planning.

Completed:
- Python virtual environment setup.
- Initial dependency installation.
- Dependency snapshot creation.
- Git repository initialization.
- Initial project directory structure.
- Requirements documentation.
- Proposed system architecture.

Pending:
- Initial application implementation.
- Symbolic reasoning module.
- Step-level error detection.
- Automated test cases.
- Streamlit user interface.

## Future Scope

- Handwritten mathematical expression recognition.
- Image-based solution input.
- Support for additional mathematical topics.
- More advanced explanation capabilities.

## License

License selection is pending.