# MathTrace AI — Explanation Engine Design

## 1. Purpose

The Explanation Engine is responsible for generating understandable mathematical feedback when an invalid transformation is detected in a student's algebraic solution.

Its purpose is not only to identify an error but also to help students understand the mathematical reason behind it.

The current implementation supports selected sign-error and arithmetic-error patterns and generates corrective feedback when the implemented logic can determine a reliable correction.

## 2. Design Principles

The Explanation Engine follows these design principles:

1. **Mathematical correctness:** Explanations should be supported by the mathematical checks performed by the system.
2. **Evidence-based feedback:** Explanations should describe observable differences between equations rather than assume the student's intentions.
3. **Clarity:** Feedback should use simple, student-friendly language.
4. **Reliable correction:** A corrected equation should only be suggested when it can be calculated using the supported mathematical logic.
5. **Uncertainty handling:** The system should avoid assigning unsupported error categories or generating unjustified corrections.
6. **Consistency:** Feedback should follow a predictable structure so the application can display it reliably.

## 3. Current Implementation

The explanation functionality is currently implemented within:

`src/mathtrace/validator.py`

The function responsible for analyzing an individual invalid transition is:

```python
explain_error(original, transformed, variable)
```

The implementation receives the equation before the transformation, the equation after the transformation, and the variable being considered.

It examines the mathematical relationship between the two equations and generates feedback for supported error patterns.

The explanation functionality is not yet maintained as an independent Python module.

## 4. Input Requirements

The `explain_error()` function receives three arguments:

- `original`: The equation before the student's transformation.
- `transformed`: The equation written by the student after the transformation.
- `variable`: The symbolic variable being solved.

For example:

```python
original = Eq(2*x, 8, evaluate=False)
transformed = Eq(x, 18, evaluate=False)
variable = x
```

This represents a transition in which the student is attempting to isolate the variable but has written an incorrect numerical result.

## 5. Error Categories

The current implementation focuses on selected mathematical error patterns.

### 5.1 Sign Error

A sign error occurs when positive or negative terms are handled incorrectly during an algebraic transformation.

The current implementation includes logic for detecting supported sign-error patterns.

### 5.2 Possible Arithmetic Error

An arithmetic error occurs when the mathematical operation is appropriate but the resulting numerical calculation appears incorrect.

The current implementation includes heuristic checks for selected arithmetic-error patterns.

For example:

```text
2*x = 8
x = 18
```

The expected result after dividing both sides by 2 is:

```text
x = 4
```

The system can identify this as a possible arithmetic error within its supported pattern.

The classification is intentionally described as *possible* because the system cannot infer the student's actual reasoning from the equations alone.

### 5.3 Incorrect Distribution

Incorrect distribution occurs when multiplication is not applied to every term inside parentheses.

This is a future classification target and is not currently implemented as a dedicated error detector.

### 5.4 Missing Division

Missing division occurs when a student attempts to isolate a variable but does not correctly divide both sides by its non-zero coefficient.

This is also a future classification target and is not currently implemented as a dedicated error detector.

## 6. Error Classification Strategy

The current explanation logic uses observable mathematical differences between consecutive equations.

Its general approach is:

1. Receive the original and transformed equations.
2. Examine relevant symbolic expressions and numerical values.
3. Apply the implemented error-detection conditions.
4. Identify a supported error category when sufficient evidence is available.
5. Generate an explanation and correction when the implemented logic can justify them.
6. Avoid forcing a specific classification when the available evidence is insufficient.

The classification process uses rule-based checks and heuristics rather than a general-purpose mathematical proof system.

An invalid transition does not automatically imply that the system can identify the exact reason for the mistake.

## 7. Feedback Structure

The explanation functionality produces structured feedback for the validator and application interface.

The feedback includes information such as:

| Field | Purpose |
|---|---|
| `status` | Indicates whether the analyzed transition is valid or invalid. |
| `error_category` | Identifies the detected category when supported. |
| `explanation` | Describes the mathematical issue in understandable language. |
| `correction` | Provides corrective guidance when available. |
| `corrected_equation` | Displays the corrected equation when it can be determined. |

### Feedback Requirements

- Valid transitions should not receive invented error explanations.
- Supported invalid transitions should receive an appropriate explanation.
- A specific error category should only be assigned when the implemented checks support it.
- Corrected equations should be generated only when the correction can be calculated reliably.
- Unsupported or ambiguous cases should not receive fabricated mathematical feedback.
- Feedback should remain understandable to students who are learning algebra.

## 8. First-Error Localization

MathTrace AI examines consecutive equations in the submitted solution.

When an invalid transition is detected, the validation logic records its position and identifies the earliest detected error.

The explanation functionality is then used to analyze that transition and generate relevant feedback.

For example:

```text
2*x + 3 = 11
2*x = 8
x = 18
```

The first transformation is valid.

The second transformation is identified as containing a possible arithmetic error.

The system therefore focuses its feedback on the transition from:

```text
2*x = 8
```

to:

```text
x = 18
```

This approach helps the student locate the earliest detected issue instead of receiving feedback only about the final answer.

## 9. Integration with the Validator

The explanation functionality works alongside the mathematical validation and error-detection logic.

### Integration Workflow

1. The application receives the student's ordered solution steps.
2. The parser converts supported text expressions into symbolic equations.
3. The validator examines consecutive equation transitions.
4. The validation logic identifies the earliest detected invalid transition.
5. The `explain_error()` function analyzes the relevant equations.
6. Structured feedback is returned to the application.
7. Streamlit displays the detected error category, explanation, and corrected equation when available.

### Current Separation of Responsibilities

Although these responsibilities are logically distinct, some of them currently share the same implementation module.

- **Parser (`parser.py`):** Handles supported mathematical input parsing.
- **Validator (`validator.py`):** Handles equation validation, selected error detection, first-error localization, and explanation generation.
- **Application (`app.py`):** Handles user interaction and feedback presentation.
- **Tests (`tests/`):** Verify parsing, validation, error detection, and feedback behavior.

A dedicated explanation module may be introduced in a future refactoring if the functionality grows.

## 10. Current Limitations

The current Explanation Engine is an experimental, rule-based implementation.

Its limitations include:

- Only selected sign-error and arithmetic-error patterns are supported.
- Error classification is not comprehensive.
- The system cannot reliably infer a student's intention.
- Some invalid transformations may not receive a specific error category.
- Corrective feedback is limited to cases supported by the implemented logic.
- Incorrect distribution and missing-division detection are not yet implemented as dedicated detectors.

These limitations must be considered when interpreting the generated feedback.

## 11. Future Improvements

Potential improvements include:

- Expanding the range of supported algebraic error categories.
- Improving the reliability of arithmetic-error classification.
- Developing dedicated detectors for distribution and coefficient-isolation errors.
- Improving explanations for multi-step transformations.
- Separating explanation generation into an independent module when appropriate.
- Evaluating feedback quality using a collection of student-style algebraic mistakes.
- Exploring more comprehensive mathematical verification techniques.

The long-term goal is to provide explanations that are mathematically justified, understandable, and useful for learning.