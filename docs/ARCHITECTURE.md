# MathTrace AI — System Architecture

## 1. Architecture Overview

MathTrace AI follows a modular architecture that separates user interaction, mathematical input processing, symbolic validation, error detection, and feedback generation.

The current prototype accepts typed algebraic solution steps and uses Python and SymPy to process and evaluate supported mathematical expressions.

The architecture is designed to keep the mathematical processing logic separate from the user interface, making the system easier to test, maintain, and extend.

## 2. Architecture Components

### 2.1 User Interface Layer

**Technology:** Streamlit

**Implementation:** `app.py`

Responsibilities:

- Accept a student's ordered algebraic solution steps.
- Provide an interactive interface for submitting solutions.
- Display the validation result.
- Show the detected error category when applicable.
- Present explanations and corrected equations for supported cases.

The interface communicates with the mathematical processing layer rather than implementing mathematical validation itself.

### 2.2 Input Processing and Parsing Layer

**Technology:** Python, Abstract Syntax Tree (AST), SymPy

**Implementation:** `src/mathtrace/parser.py`

Responsibilities:

- Receive typed algebraic solution steps.
- Validate the structure of mathematical input.
- Parse supported mathematical expressions safely.
- Support the currently implemented variable and mathematical operators.
- Convert accepted expressions into SymPy representations.
- Handle malformed or unsupported expressions without evaluating arbitrary Python code.

The current parser supports the variable `x`, numeric values, parentheses, arithmetic operators, and explicit multiplication.

For example:

```text
2*x + 3 = 11
```

Implicit multiplication, such as `2x`, is not currently supported.

### 2.3 Symbolic Validation Layer

**Technology:** Python and SymPy

**Implementation:** `src/mathtrace/validator.py`

Responsibilities:

- Represent equations using SymPy.
- Compare mathematical relationships between consecutive solution steps.
- Use symbolic operations and solution-set comparisons in the supported validation process.
- Determine whether consecutive equations are considered equivalent under the current validation approach.
- Provide validation results to the error-detection process.

Symbolic processing allows the system to examine mathematical expressions rather than relying only on textual comparison.

However, equivalence checking alone does not establish that every individual transformation is mathematically justified.

### 2.4 Error Detection Layer

**Technology:** Python and SymPy

**Implementation:** `src/mathtrace/validator.py`

Responsibilities:

- Examine consecutive equations in the submitted solution.
- Detect selected sign-error patterns.
- Identify possible arithmetic errors for supported cases.
- Locate the earliest detected invalid transition.
- Avoid assigning an error category when the available evidence is insufficient for a supported classification.

The current implementation uses rule-based checks and heuristics. It does not provide universal mathematical error detection.

### 2.5 Explanation and Feedback Layer

**Technology:** Python and SymPy

**Implementation:** `src/mathtrace/validator.py`

Responsibilities:

- Determine the detected error category.
- Generate an understandable explanation for supported errors.
- Calculate a corrected equation when the implemented logic can justify one.
- Return structured feedback to the application interface.

The feedback system currently focuses on selected sign and arithmetic errors.

### 2.6 Testing Layer

**Technology:** pytest

**Implementation:** `tests/`

Responsibilities:

- Test mathematical expression parsing.
- Test equation validation.
- Verify selected sign-error and arithmetic-error detection patterns.
- Test first-error localization.
- Test malformed and unsupported inputs.
- Verify feedback generation.
- Prevent previously identified bugs from reappearing through regression tests.

The current automated test suite contains 50 passing tests.

## 3. Technology Stack

| Component | Technology | Purpose |
|---|---|---|
| Programming language | Python 3.12 | Core application logic |
| Symbolic mathematics | SymPy | Mathematical expression and equation processing |
| User interface | Streamlit | Interactive application |
| Expression parsing | Python AST | Safe input parsing |
| Automated testing | pytest | Unit and integration testing |
| Image processing foundation | Pillow | Potential future image-processing work |
| Version control | Git and GitHub | Source-code management |

Pillow is included as a foundation for potential future image-processing functionality. Handwriting recognition and OCR are not currently implemented.

## 4. System Processing Flow

The current application follows this processing sequence:

1. **Student Input:** The student enters an ordered sequence of typed algebraic equations through the Streamlit interface.
2. **Input Parsing:** The parser validates the input and converts supported expressions into SymPy representations.
3. **Step Validation:** The validation logic examines relationships between consecutive equations.
4. **Error Detection:** Selected rule-based checks identify supported sign and arithmetic errors.
5. **Error Localization:** The system identifies the earliest detected invalid transition.
6. **Explanation Generation:** The feedback logic generates an explanation and a corrected equation when possible.
7. **Result Presentation:** Streamlit displays the validation result and available feedback.

## 5. Component Interaction

The following diagram represents the current high-level processing flow:

```text
             Student
                |
                v
       Streamlit Interface
             app.py
                |
                v
       Input Processing
          parser.py
                |
                v
       Symbolic Validation
         validator.py
                |
                v
        Error Detection
         validator.py
                |
                v
      Explanation Generation
         validator.py
                |
                v
       Feedback to Student
                |
                v
        Streamlit Interface


       Automated Testing
             pytest
                |
                v
       Parser and Validator
```

The parser and validator are separate modules, while validation, error detection, and explanation generation currently share the `validator.py` module.

## 6. Design Principles

- **Modularity:** Separate input parsing, mathematical validation, and user interaction.
- **Mathematical Reliability:** Use symbolic mathematical operations wherever applicable.
- **Explainability:** Provide understandable feedback for detected errors.
- **Testability:** Keep core processing functions independently testable.
- **Safe Input Handling:** Parse supported expressions without executing arbitrary Python code.
- **Honest Error Classification:** Avoid claiming a specific error category when the available checks cannot establish it reliably.
- **Maintainability:** Keep module responsibilities and interfaces clear.

## 7. Current Implementation Status

| Component | Status |
|---|---|
| Streamlit user interface | Implemented |
| Typed expression parser | Implemented |
| SymPy equation processing | Implemented |
| Consecutive-step validation | Implemented |
| Selected sign-error detection | Implemented |
| Selected arithmetic-error detection | Implemented |
| First-error localization | Implemented |
| Explanation and correction generation | Implemented for supported cases |
| Automated testing | Implemented — 50 tests passing |
| Handwriting recognition | Not implemented |
| Mathematical OCR | Not implemented |

## 8. Current Architectural Limitations

The architecture currently supports a limited prototype rather than a general-purpose mathematics verification system.

- The currently supported variable is `x`.
- Multiplication must be written explicitly.
- Error detection covers selected patterns rather than all algebraic mistakes.
- Some mathematically incorrect transformations may not receive a specific error classification.
- The system does not currently provide comprehensive proof-based verification of every transformation.
- Handwritten mathematical input and image processing are outside the implemented scope.

These limitations will guide future architectural improvements.

## 9. Future Architectural Extensions

Potential future extensions include:

- A dedicated mathematical OCR and handwriting-recognition component.
- Expanded expression parsing and variable support.
- A more comprehensive transformation-verification engine.
- Improved error classification and explanation generation.
- Additional mathematical domains.
- Evaluation using a larger dataset of student-written solutions.

The architecture will evolve as these capabilities are researched, designed, and implemented.