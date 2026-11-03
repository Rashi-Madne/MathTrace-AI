# Explanation Engine Design

## 1. Purpose

The Explanation Engine is responsible for generating understandable mathematical feedback when a student makes an incorrect transformation while solving an equation.

Its goal is not only to identify an error but also to help students understand the mathematical reason behind it.

## 2. Design Principles

The Explanation Engine should follow these principles:

1. **Mathematical correctness:** Every explanation must be supported by mathematical verification.
2. **Evidence-based feedback:** Explanations must be based on the observed equations rather than assumptions about the student's intentions.
3. **Clarity:** Feedback should use simple, student-friendly language.
4. **Reliable correction:** A corrected equation should only be suggested when it can be determined reliably.
5. **Uncertainty handling:** The system should avoid generating unsupported explanations.

## 3. Input Requirements

The Explanation Engine should receive:

- `original`: The equation before the student's transformation.
- `transformed`: The equation written by the student.
- `variable`: The variable being solved.

## 4. Expected Output

The Explanation Engine should produce structured feedback containing:

- Status of the transition.
- Description of the mathematical issue.
- Explanation of why the transition is incorrect.
- Suggested correction, when reliable.

For valid transitions, it should report that no mathematical error was detected.

For unsupported or ambiguous transitions, it should communicate that the error could not be reliably explained.

## 5. Proposed Function Interface

The initial function interface is:

`explain_error(original, transformed, variable)`

The implementation will be developed after the mathematical analysis and error-classification strategy have been defined.

## 6. Important Limitation

The system can analyse mathematical expressions and identify observable errors. However, it cannot reliably determine what a student was thinking or intending from the equations alone.

Therefore, feedback must describe the mathematical evidence rather than assume the student's intention.


## 7. Initial Error Categories

The initial version of MathTrace AI will explore the following mathematical error categories:

### 7.1 Sign Error
Incorrect handling of positive and negative terms during equation transformations.

### 7.2 Arithmetic Error
Incorrect numerical calculation during an otherwise appropriate mathematical operation.

### 7.3 Incorrect Distribution
Failure to apply multiplication to every term within a set of parentheses.

### 7.4 Missing Division
Failure to divide both sides by the non-zero coefficient when isolating a variable.

**Important:** These categories represent initial classification targets. The system must use mathematical evidence to assign a category and should avoid classification when the available evidence is insufficient.


## 8. Error Classification Strategy

MathTrace AI should classify mathematical errors using observable differences between the original and transformed equations.

The classification process should follow these principles:

1. Examine the original and transformed equations.
2. Identify the mathematical difference between them.
3. Compare the observed difference with the supported error categories.
4. Assign a category only when sufficient mathematical evidence is available.
5. Avoid forcing an error category when the mistake is ambiguous or unsupported.

### Classification Reliability

The system should distinguish between:

- **Identified error:** A supported mathematical error category can be assigned.
- **Unclassified error:** An invalid transition is detected, but its exact error category cannot be determined reliably.
- **Unable to verify:** The mathematical transition itself cannot be evaluated reliably.

An incorrect transition must not automatically be assigned an error category merely because it is invalid.


## 9. Structured Feedback Format

The Explanation Engine should return feedback in a consistent structured format.

The proposed output fields are:

| Field | Purpose |
|---|---|
| `status` | Indicates whether the transition is valid, invalid, or unable to verify. |
| `error_category` | Identifies the detected error category when supported. |
| `explanation` | Describes the mathematical issue in understandable language. |
| `correction` | Provides the recommended mathematical operation when reliable. |
| `corrected_equation` | Displays the corrected equation when it can be determined. |

### Output Requirements

- Valid transitions should not contain invented error explanations.
- Invalid transitions should include an explanation when sufficient evidence is available.
- Unsupported or ambiguous cases should communicate uncertainty.
- Optional fields should be left empty or represented as null when they cannot be determined reliably.

The output structure should remain consistent across different feedback outcomes.


## 10. Integration with the Validator

The Explanation Engine will work alongside the existing mathematical validator.

**Integration workflow:**

1. Receive the student's sequence of equations.
2. Use the Validator to evaluate consecutive equation transitions.
3. Identify the first invalid transition, if one exists.
4. Pass the relevant equations to the Explanation Engine.
5. Analyse the mathematical difference and classify the error when sufficient evidence is available.
6. Generate structured, student-friendly feedback.
7. Return the final feedback to the application interface.

### Separation of Responsibilities

- The Validator is responsible for mathematical verification and error localization.
- The Explanation Engine is responsible for interpreting detected errors and generating explanations.
- The application interface is responsible for presenting the feedback to the student.

The Explanation Engine must not override the Validator's mathematical verification result.