# MathTrace AI — Supported Algebraic Transformations

## 1. Purpose

This document describes the fundamental algebraic transformation rules relevant to MathTrace AI and distinguishes between mathematical rules and the capabilities currently implemented in the prototype.

The mathematical examples focus on single-variable linear equations.

The current implementation accepts typed equations using the variable `x` and evaluates supported mathematical expressions using Python and SymPy.

Importantly, a mathematically valid transformation rule is not necessarily an independently implemented transformation detector.

## 2. Fundamental Algebraic Transformation Rules

### Rule 1: Addition on Both Sides

**Description:**

The same constant may be added to both sides of an equation without changing its solution set.

**Example:**

Original equation:

```text
x + 2 = 5
```

Transformation:

```text
x + 2 + 3 = 5 + 3
```

Simplified equation:

```text
x + 5 = 8
```

**Expected mathematical result:** Valid transformation.

**Mathematical condition:** The same constant must be added to both sides.

**Current implementation status:** The validator can compare supported equations for mathematical equivalence. It does not yet have a dedicated addition-on-both-sides transformation detector.

### Rule 2: Subtraction on Both Sides

**Description:**

The same constant may be subtracted from both sides of an equation without changing its solution set.

**Example:**

Original equation:

```text
x + 5 = 8
```

Transformation:

```text
x + 5 - 5 = 8 - 5
```

Simplified equation:

```text
x = 3
```

**Expected mathematical result:** Valid transformation.

**Mathematical condition:** The same constant must be subtracted from both sides.

**Current implementation status:** The validator can compare supported equations for mathematical equivalence. It does not yet have a dedicated subtraction-on-both-sides transformation detector.

### Rule 3: Multiplication on Both Sides

**Description:**

Both sides of an equation may be multiplied by the same non-zero constant without changing the solution set.

**Example:**

Original equation:

```text
x + 2 = 5
```

Transformation:

```text
3*(x + 2) = 3*5
```

Simplified equation:

```text
3*x + 6 = 15
```

**Expected mathematical result:** Valid transformation.

**Mathematical condition:** The same non-zero constant must multiply both sides.

**Current implementation status:** Symbolic expression processing supports multiplication. However, the system does not yet independently identify and classify every multiplication-on-both-sides operation.

### Rule 4: Division on Both Sides

**Description:**

Both sides of an equation may be divided by the same non-zero constant without changing the solution set.

**Example:**

Original equation:

```text
2*x = 8
```

Transformation:

```text
(2*x)/2 = 8/2
```

Simplified equation:

```text
x = 4
```

**Expected mathematical result:** Valid transformation.

**Mathematical condition:** The same non-zero constant must divide both sides.

**Current implementation status:** Symbolic expression processing supports division. The validator does not yet have a dedicated detector for every division-on-both-sides operation.

### Rule 5: Algebraic Simplification

**Description:**

An algebraic expression may be rewritten into an equivalent expression without changing its mathematical value.

**Example:**

Original equation:

```text
2*x + 3*x = 10
```

Simplified equation:

```text
5*x = 10
```

**Expected mathematical result:** Valid transformation.

**Mathematical condition:** The expressions on both sides must remain mathematically equivalent.

**Current implementation status:** SymPy supports symbolic simplification and expression processing. The current validator uses symbolic mathematical comparisons, but it does not independently recognize every possible simplification rule.

## 3. Current Error-Detection Capabilities

In addition to evaluating supported equation relationships, MathTrace AI implements selected error-detection checks.

| Error category | Current status |
|---|---|
| Selected sign errors | Implemented |
| Selected arithmetic errors | Implemented |
| Incorrect distribution | Not implemented as a dedicated detector |
| Missing division | Not implemented as a dedicated detector |
| General algebraic transformation errors | Not comprehensively supported |

The implemented error detectors use rule-based conditions and heuristics. They should not be interpreted as comprehensive coverage of the listed error categories.

## 4. Mathematical Verification Approach

MathTrace AI uses SymPy to represent and process mathematical equations.

The current validation approach examines the mathematical relationship between consecutive equations rather than relying only on textual comparison.

This allows mathematically equivalent expressions to be evaluated using symbolic operations.

However, equation equivalence and transformation validity are related but distinct concepts.

Two equations can have the same solution set without proving that the student's particular intermediate operation was justified.

Therefore, the current system should be understood as a limited symbolic validation and error-detection prototype, not a complete algebraic proof engine.

## 5. Input Syntax Restrictions

The current expression parser supports a defined subset of mathematical syntax.

| Feature | Current support |
|---|---|
| Variable `x` | Supported |
| Integer and decimal values | Supported |
| Addition and subtraction | Supported |
| Multiplication | Supported |
| Division | Supported |
| Parentheses | Supported |
| Explicit multiplication | Supported |
| Implicit multiplication, such as `2x` | Not supported |
| Multiple variables | Not currently supported |

Examples of accepted notation:

```text
2*x + 3 = 11
```

```text
(x + 2)/2 = 4
```

Examples outside the current syntax:

```text
2x + 3 = 11
```

## 6. Current Implementation Limitations

- The current parser supports only the variable `x`.
- Mathematical syntax is restricted to the implemented expression grammar.
- Not every fundamental algebraic rule has a dedicated transformation detector.
- Error classification is limited to selected patterns.
- Some invalid transformations may not receive a specific error category.
- Symbolic equivalence does not establish the validity of every intermediate mathematical operation.
- The system does not yet provide comprehensive mathematical proof generation.

## 7. Future Development

Potential improvements include:

1. Implementing dedicated detectors for individual algebraic transformation rules.
2. Expanding support for linear equation transformations.
3. Improving the detection of incorrect distribution and coefficient-isolation errors.
4. Supporting additional variables and mathematical expression formats.
5. Introducing more comprehensive mathematical verification.
6. Evaluating transformation detection using a collection of valid and invalid student solutions.

The supported transformation set will be expanded only after each capability has been implemented and tested.

## 8. Conclusion

This document establishes the mathematical foundation and current scope of MathTrace AI.

It separates fundamental algebraic principles from the limited set of capabilities implemented in the current prototype.

This distinction helps ensure that the project's documentation accurately represents its mathematical capabilities and provides a clear direction for future development.