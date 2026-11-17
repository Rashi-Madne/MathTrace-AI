# MathTrace AI — Project Requirements

## 1. Project Overview

MathTrace AI is an experimental mathematics learning assistant designed to analyze a student's step-by-step algebraic solution, identify the earliest detected incorrect mathematical transformation, and provide understandable feedback.

Unlike conventional answer-checking systems that focus primarily on the final answer, MathTrace AI examines relationships between consecutive solution steps.

The current prototype uses Python and SymPy for mathematical expression processing and rule-based checks for selected error patterns.

## 2. Problem Statement

Students may arrive at an incorrect answer because of a mistake made during an intermediate mathematical transformation.

Traditional answer-checking systems may identify that the final answer is incorrect without explaining where the reasoning first became invalid.

MathTrace AI explores how symbolic mathematics and step-level error detection can help identify the earliest incorrect transition and provide useful corrective feedback.

## 3. Project Objectives

The project aims to:

1. Accept a student's sequence of typed algebraic solution steps.
2. Parse supported mathematical expressions safely.
3. Represent equations using symbolic mathematical expressions.
4. Evaluate relationships between consecutive solution steps.
5. Identify the earliest detected invalid transition.
6. Detect selected mathematical error patterns.
7. Generate understandable explanations for supported errors.
8. Provide a corrected equation when the implemented logic can determine one reliably.
9. Handle malformed and unsupported input safely.
10. Develop a testable and maintainable mathematical processing system.

## 4. Functional Requirements

The following table distinguishes implemented functionality from requirements that need further development.

| ID | Requirement | Status |
|---|---|---|
| FR-01 | The system shall accept multiple typed algebraic solution steps. | Implemented |
| FR-02 | The system shall validate the structure of submitted input. | Implemented |
| FR-03 | The system shall parse supported algebraic expressions into symbolic representations. | Implemented |
| FR-04 | The system shall evaluate mathematical relationships between consecutive equations. | Implemented |
| FR-05 | The system shall identify the earliest detected invalid transition. | Implemented |
| FR-06 | The system shall detect selected sign-error patterns. | Implemented |
| FR-07 | The system shall detect possible arithmetic errors for supported patterns. | Implemented |
| FR-08 | The system shall generate explanations for supported error categories. | Implemented |
| FR-09 | The system shall generate corrected equations when supported by the implemented logic. | Implemented |
| FR-10 | The system shall provide an interactive interface for submitting and reviewing solutions. | Implemented |
| FR-11 | The system shall handle malformed or unsupported expressions safely. | Implemented |
| FR-12 | The system shall provide comprehensive verification of all algebraic transformations. | Future improvement |
| FR-13 | The system shall support a comprehensive uncertain-transition feedback outcome. | Future improvement |
| FR-14 | The system shall support handwritten mathematical solution input. | Future improvement |

The implemented error-detection functionality is limited to selected patterns. It does not provide comprehensive mathematical error classification.

## 5. Non-Functional Requirements

### 5.1 Mathematical Reliability

Mathematical decisions should be based on symbolic operations and explicitly implemented validation rules.

The system should avoid presenting unsupported mathematical conclusions as verified results.

### 5.2 Usability

The interface should be understandable to students who are learning algebra.

Feedback should identify the relevant step and present explanations in clear language.

### 5.3 Reliability

The application should handle malformed and unsupported input without unexpected crashes.

### 5.4 Maintainability

The source code should be organized into modules with clearly defined responsibilities.

### 5.5 Testability

Core parsing, validation, error-detection, and feedback functions should have automated tests.

### 5.6 Transparency

The system should communicate the limitations of its implemented mathematical checks and avoid claiming capabilities it does not possess.

### 5.7 Safety

Mathematical input should be parsed using controlled parsing logic rather than executed as arbitrary Python code.

## 6. Project Scope

### 6.1 Included in the Current Prototype

- Typed algebraic equation input.
- Step-by-step solution analysis.
- Safe parsing using Python AST.
- Symbolic mathematical processing using SymPy.
- Consecutive-equation validation.
- Earliest detected error localization.
- Selected sign-error detection.
- Selected arithmetic-error detection.
- Rule-based explanation generation.
- Corrected-equation generation for supported cases.
- Streamlit-based user interface.
- Automated testing using pytest.

### 6.2 Current Input Restrictions

The current implementation supports:

- A single variable: `x`.
- Integer and decimal values.
- Addition and subtraction.
- Multiplication and division.
- Parentheses.
- Explicit multiplication, such as `2*x`.

Implicit multiplication, such as `2x`, is not currently supported.

### 6.3 Deferred Features

The following features are outside the current implementation:

- Handwritten mathematical expression recognition.
- OCR-based solution input.
- Image-based mathematical solution processing.
- Multiple-variable equation support.
- Comprehensive algebraic transformation verification.
- Dedicated detectors for every mathematical error category.
- Advanced mathematical topics.
- Large language model integration, unless future research establishes a justified need.

## 7. Initial Success Criteria

The prototype is evaluated through automated tests and manual application checks.

The intended success criteria are:

1. Supported mathematical expressions are parsed correctly.
2. Valid equation transitions pass the implemented validation checks.
3. Selected invalid transformations are detected.
4. The earliest detected invalid transition is correctly localized.
5. Supported error categories receive understandable explanations.
6. Corrected equations are generated correctly for supported cases.
7. Malformed and unsupported input is handled safely.
8. Previously identified bugs are covered by regression tests.

### Current Verification Snapshot

The current automated test suite reports:

| Metric | Result |
|---|---:|
| Total automated tests passed | 50 |
| Failed tests | 0 |
| Automated test framework | pytest |

This result demonstrates that the current test cases pass. It does not establish comprehensive accuracy across all algebraic problems or student error patterns.

## 8. Scope and Limitations

MathTrace AI is currently an experimental prototype focused on a limited subset of typed, single-variable algebraic equations.

Important limitations include:

- Only the variable `x` is currently supported.
- Mathematical syntax is restricted to the implemented parser grammar.
- Error classification uses rule-based checks and heuristics.
- Not every invalid transformation can be assigned a specific error category.
- Symbolic equation equivalence does not necessarily prove that every intermediate operation was justified.
- The system does not currently provide comprehensive mathematical proof generation.
- Handwritten input and OCR are not implemented.

The system must distinguish between mathematical equivalence and the validity of a particular transformation.

Two equations may have the same solution set without establishing that the student's intermediate operation was mathematically justified.

## 9. Future Development Goals

Potential future improvements include:

1. Expanding the supported algebraic expression grammar.
2. Supporting additional variables.
3. Developing dedicated detectors for more mathematical error categories.
4. Improving the reliability of transformation verification.
5. Introducing more comprehensive uncertainty handling.
6. Improving the quality and detail of mathematical explanations.
7. Exploring handwritten mathematical expression recognition.
8. Evaluating the system using a larger dataset of student-generated solutions.

Future capabilities will be added only after their mathematical requirements have been defined and their implementations have been tested.

## 10. Conclusion

MathTrace AI aims to make mathematical solution checking more informative by focusing on intermediate reasoning rather than only final answers.

The current prototype establishes a foundation through safe expression parsing, symbolic validation, selected error detection, corrective feedback, and automated testing.

These requirements provide a clear boundary between the capabilities already implemented and the improvements planned for future development.