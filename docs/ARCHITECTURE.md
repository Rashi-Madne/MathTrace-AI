# MathTrace AI - System Architecture

## 1. Architecture Overview

MathTrace AI will use a modular architecture that separates user interaction, mathematical input processing, symbolic verification, error detection, and explanation generation.

The initial implementation will focus on typed algebraic input and symbolic reasoning.

## 2. Main Components

### 2.1 User Interface

Technology: Streamlit

Responsibilities:
- Accept the original algebraic problem.
- Accept the student's solution steps.
- Display analysis results.
- Present explanations and corrections.

### 2.2 Input Processing Module

Technology: Python

Responsibilities:
- Receive the problem and solution steps.
- Validate input structure.
- Prepare supported mathematical expressions for parsing.
- Handle invalid or unsupported expressions safely.

### 2.3 Symbolic Reasoning Module

Technology: SymPy

Responsibilities:
- Parse supported algebraic expressions.
- Represent mathematical expressions symbolically.
- Evaluate relationships between consecutive solution steps.
- Support mathematical verification without relying only on textual comparison.
- Account for mathematical equivalence, solution sets, and relevant domain restrictions when verifying transformations. 


### 2.4 Error Detection Module

Technology: Python and SymPy

Responsibilities:
- Analyze consecutive solution steps.
- Determine whether a transformation is mathematically justified within the supported scope.
- Identify the earliest detected invalid transformation.
- Distinguish incorrect steps from uncertain or unsupported cases.
- Classify each evaluated transformation as valid, invalid, unsupported, or ambiguous when sufficient evidence is available.

### 2.5 Explanation Module

Technology: Python

Responsibilities:
- Describe the identified mathematical error.
- Explain why the transformation is invalid.
- Generate a justified correction when possible.
- Present feedback in understandable language.

### 2.6 Testing Module

Technology: pytest

Responsibilities:
- Test mathematical expression handling.
- Test valid and invalid transformations.
- Verify earliest-error detection.
- Test malformed and unsupported input.
- Prevent regressions when the implementation changes.

## 3. Initial Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python 3.12 |
| Symbolic mathematics | SymPy |
| User interface | Streamlit |
| Automated testing | pytest |
| Image processing foundation | Pillow |
| Version control | Git and GitHub |

Pillow is installed for potential future image-processing work. Handwriting recognition is outside the initial prototype scope.

## 4. Proposed Processing Flow

1. The student submits an algebraic problem and ordered solution steps.
2. The input module validates and parses the supported expressions.
3. The symbolic reasoning module evaluates consecutive transformations.
4. The error detection module identifies the earliest invalid transformation when it can establish one.
5. The explanation module prepares mathematical feedback.
6. The user interface displays the analysis.

## 5. Design Principles

- Modularity: Each major responsibility should be implemented separately.
- Mathematical correctness: Decisions must be based on justified mathematical checks.
- Explainability: Detected errors should have understandable explanations.
- Testability: Core reasoning functions should be independently testable.
- Safe handling: Unsupported cases should be reported rather than guessed.
- Maintainability: Modules should have clear responsibilities and interfaces.

## 6. Current Implementation Status

This document describes the proposed architecture. The components and processing flow have not yet been implemented.

The architecture will be updated as implementation decisions and mathematical requirements become clearer.