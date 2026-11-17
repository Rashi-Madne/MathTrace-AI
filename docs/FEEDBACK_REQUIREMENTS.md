# MathTrace AI — Feedback Requirements

## 1. Purpose

This document defines how MathTrace AI communicates the results of evaluating a student's algebraic solution.

The goal is to provide understandable, useful, and mathematically grounded feedback.

The system focuses on identifying the earliest detected incorrect transition rather than checking only the final answer.

These requirements describe both the current feedback capabilities and the desired behaviour for future improvements.

## 2. Feedback Outcomes

MathTrace AI aims to support three main feedback outcomes.

### 2.1 Valid Solution

**Condition:**

All consecutive equation transitions pass the current validation checks.

**Expected behaviour:**

- Indicate that all checked solution steps passed validation.
- Avoid displaying unnecessary error explanations.
- Present a clear success message.

**Current implementation:**

The application displays:

```text
All solution steps passed validation.
```

This message indicates that the submitted transitions passed the implemented checks. It does not guarantee that every possible mathematical operation has been independently proven valid.

### 2.2 Invalid Solution

**Condition:**

A consecutive equation transition is identified as invalid by the current validation logic.

**Expected behaviour:**

- Identify the earliest detected invalid transition.
- Display the relevant equation before the transformation.
- Display the student's transformed equation.
- Show the detected error category when supported.
- Explain the mathematical issue.
- Provide a corrected equation when the implemented logic can determine one reliably.

**Current implementation:**

The application supports selected sign-error and possible arithmetic-error feedback patterns.

### 2.3 Unable to Verify

**Condition:**

The system cannot reliably evaluate an expression or mathematical transition within its supported scope.

**Expected behaviour:**

- Avoid making an unsupported valid or invalid decision.
- Communicate that the input could not be evaluated reliably.
- Identify unsupported or malformed input when possible.
- Avoid inventing a mathematical explanation or correction.

**Current implementation:**

The parser handles malformed and unsupported expressions through input-validation and error-handling logic.

A comprehensive, separate `unable_to_verify` feedback outcome for every uncertain mathematical transition remains a future improvement.

## 3. Step-Level Feedback

MathTrace AI evaluates consecutive equations instead of relying only on the final answer.

**Expected behaviour:**

- Examine each transition between consecutive equations.
- Identify the earliest detected invalid transition.
- Preserve the validation results of earlier transitions.
- Avoid presenting later transitions as successfully verified after an earlier invalid transition has been identified.
- Provide the equations involved in the detected transition.

**Example:**

Student solution:

```text
2*x + 3 = 11
2*x = 8
x = 5
```

Expected analysis:

| Transition | Expected result |
|---|---|
| `2*x + 3 = 11` → `2*x = 8` | Valid |
| `2*x = 8` → `x = 5` | Invalid |

The first incorrect transition is from:

```text
2*x = 8
```

to:

```text
x = 5
```

The mathematically correct result is:

```text
x = 4
```

The current implementation localizes the earliest detected invalid transition and generates feedback for supported error patterns.

## 4. Mathematical Error Explanation

When an invalid transition is detected, MathTrace AI should explain the observable mathematical issue.

**Expected behaviour:**

- Describe the detected mathematical error when a supported category is available.
- Explain why the transformation is incorrect.
- Suggest the appropriate operation when it can be determined.
- Provide a corrected equation when reliable.
- Use simple, student-friendly language.
- Avoid assuming the student's intention.
- Avoid presenting uncertain explanations as established mathematical facts.

### Example: Sign Error

Original equation:

```text
2*x + 3 = 11
```

Student's transformed equation:

```text
2*x = 14
```

Expected feedback:

- **Error category:** Sign error, if supported by the implemented detection conditions.
- **Explanation:** The constant term was not moved to the other side using the correct inverse operation.
- **Correction:** Subtract 3 from both sides.
- **Corrected equation:**

```text
2*x = 8
```

The example illustrates the intended feedback style. The actual classification depends on the implemented detection conditions.

## 5. Corrective Feedback Requirements

Corrections should be mathematically justified and consistent with the identified error.

**Expected behaviour:**

- Calculate the corrected result using the supported mathematical logic.
- Preserve the equation's mathematical meaning.
- Display the corrected equation clearly.
- Avoid suggesting a correction when the system cannot determine one reliably.
- Keep the explanation consistent with the corrected equation.

For example:

```text
Original equation: 2*x = 8
Student's equation: x = 18
Corrected equation: x = 4
```

The correction is obtained by dividing both sides of the original equation by 2.

## 6. Reliability and Input Limitations

MathTrace AI should prioritise reliable feedback over producing an explanation for every input.

**Requirements:**

- Evaluate only expressions supported by the current parser.
- Handle malformed input safely.
- Avoid guessing when a transition cannot be evaluated reliably.
- Avoid assigning unsupported error categories.
- Generate corrections only when the implemented logic supports them.
- Clearly communicate the limitations of the prototype.
- Avoid claiming that every algebraic transformation has been verified.

### Current Input Scope

The current parser supports:

- The variable `x`.
- Integer and decimal values.
- Addition and subtraction.
- Multiplication and division.
- Parentheses.
- Explicit multiplication, such as `2*x`.

Implicit multiplication, such as `2x`, and multiple variables are outside the current parser's supported scope.

## 7. Feedback Presentation Requirements

The Streamlit interface should present feedback in a way that is easy for students to understand.

**Expected behaviour:**

- Use clear status messages.
- Identify the relevant solution step.
- Separate the error category from its explanation.
- Display corrected equations distinctly.
- Avoid unnecessarily complicated mathematical terminology.
- Keep valid-solution and invalid-solution feedback visually distinguishable.

The current interface displays validation results and the available explanation and correction for supported errors.

## 8. Current Implementation Status

| Feedback capability | Status |
|---|---|
| Valid-solution success message | Implemented |
| Invalid-transition detection | Implemented |
| Earliest detected error localization | Implemented |
| Selected sign-error explanation | Implemented |
| Selected arithmetic-error explanation | Implemented |
| Corrected-equation generation for supported cases | Implemented |
| Malformed-input handling | Implemented |
| Comprehensive uncertain-transition outcome | Future improvement |
| Feedback for all algebraic error categories | Future improvement |
| Complete step-by-step explanation of every operation | Future improvement |

## 9. Future Improvements

Potential improvements include:

1. Developing a more comprehensive `unable_to_verify` outcome.
2. Supporting additional algebraic error categories.
3. Improving the mathematical reliability of error classification.
4. Providing more detailed explanations of individual transformations.
5. Improving feedback for ambiguous and unsupported cases.
6. Evaluating explanation quality using a larger collection of student solutions.
7. Making the feedback interface more informative and accessible.

## 10. Conclusion

Feedback is a central part of MathTrace AI because the project aims to support mathematical learning rather than simply report whether a final answer is correct.

The current prototype provides selected step-level error explanations and corrections.

Future development will focus on improving the reliability, coverage, and educational usefulness of this feedback.