# Feedback Requirements

## 1. Purpose

This document defines how MathTrace AI should communicate the results of checking a student's mathematical solution.

The system should provide clear, understandable, and mathematically grounded feedback.

## 2. Feedback Outcomes

MathTrace AI should support three feedback outcomes.

### 2.1 Valid Solution

**Condition:** All consecutive equation transitions preserve the original solution set.

**Expected behaviour:**
- Mark the solution as valid.
- Confirm that all checked transitions are mathematically valid.
- Display the final answer when it can be determined.

### 2.2 Invalid Solution

**Condition:** At least one consecutive equation transition changes the solution set.

**Expected behaviour:**
- Mark the solution as invalid.
- Identify the first incorrect transition.
- Explain why the transition is mathematically incorrect.
- Show a corrected transformation when it can be determined reliably.

### 2.3 Unable to Verify

**Condition:** The system cannot reliably evaluate a mathematical transition.

**Expected behaviour:**
- Avoid making an unsupported valid or invalid decision.
- Clearly explain that the transition could not be verified.
- Request a clearer or supported mathematical expression when appropriate.


## 3. Step-Level Feedback

MathTrace AI should evaluate consecutive equation transitions individually rather than checking only the final answer.

**Expected behaviour:**

- Check each transition between two consecutive equations.
- Identify the first incorrect transition.
- Preserve the results of previously verified transitions.
- Stop claiming later transitions are valid when an earlier transition has already failed.
- Report the original equation and the student's transformed equation for the incorrect transition.

**Example:**

Original solution:

1. 2x + 3 = 11
2. 2x = 8
3. x = 5

Expected result:

- Transition 1 → 2: Valid.
- Transition 2 → 3: Invalid.
- First incorrect transition: 2 → 3.
- Correct result: x = 4.


## 4. Mathematical Error Explanation

When an invalid transition is detected, MathTrace AI should provide an understandable explanation of the mathematical mistake.

**Expected behaviour:**

- Describe the mathematical operation or transformation that appears to be incorrect.
- Explain why the student's transformation is invalid.
- Provide the correct transformation when it can be determined reliably.
- Use simple, student-friendly language.
- Avoid generating explanations that are not supported by mathematical verification.

**Example:**

Original equation:

2x + 3 = 11

Student's transformed equation:

2x = 14

Expected feedback:

- Error: Incorrect handling of the constant term.
- Explanation: The student added 3 instead of subtracting 3 from both sides.
- Correction: Subtract 3 from both sides.
- Correct equation: 2x = 8.


## 5. Reliability and Limitations

MathTrace AI should prioritise mathematical correctness and reliable feedback over producing an answer for every input.

**Expected behaviour:**

- Evaluate only mathematical expressions supported by the current system.
- Avoid guessing when a transformation cannot be verified reliably.
- Return an `unable_to_verify` outcome for unsupported or ambiguous cases.
- Clearly communicate the limitations of the current system.
- Ensure that suggested corrections preserve mathematical equivalence.
- Never present an unverified explanation as a mathematically established fact.

**Initial Scope:**

The first version of MathTrace AI will focus on basic single-variable linear equations over the real numbers.

Support for more advanced mathematical expressions may be introduced in future versions.