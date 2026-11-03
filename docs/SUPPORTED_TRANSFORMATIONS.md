# Supported Algebraic Transformations

## 1. Purpose

This document defines the algebraic transformations that the initial version of MathTrace AI is designed to recognise and verify.

The system will initially focus on basic single-variable linear equations over the real numbers.

## 2. Supported Transformation Rules

### Rule 1: Addition on Both Sides

**Description:** A constant may be added to both sides of an equation without changing its solution set.

**Example:**

Original equation:

x + 2 = 5

Transformed equation:

x + 2 + 3 = 5 + 3

Simplified equation:

x + 5 = 8

**Expected result:** Valid transformation.

**Mathematical condition:** The same constant must be added to both sides.


### Rule 2: Subtraction on Both Sides

**Description:** A constant may be subtracted from both sides of an equation without changing its solution set.

**Example:**

Original equation:

x + 5 = 8

Transformed equation:

x + 5 - 5 = 8 - 5

Simplified equation:

x = 3

**Expected result:** Valid transformation.

**Mathematical condition:** The same constant must be subtracted from both sides.


### Rule 3: Multiplication on Both Sides

**Description:** Both sides of an equation may be multiplied by the same non-zero constant without changing the solution set.

**Example:**

Original equation:

x + 2 = 5

Transformed equation:

3(x + 2) = 3(5)

Simplified equation:

3x + 6 = 15

**Expected result:** Valid transformation.

**Mathematical condition:** The same non-zero constant must multiply both sides.


### Rule 4: Division on Both Sides

**Description:** Both sides of an equation may be divided by the same non-zero constant without changing its solution set.

**Example:**

Original equation:

2x = 8

Transformed equation:

(2x)/2 = 8/2

Simplified equation:

x = 4

**Expected result:** Valid transformation.

**Mathematical condition:** The same non-zero constant must divide both sides.


### Rule 5: Algebraic Simplification

**Description:** Algebraic expressions may be rewritten into simpler equivalent forms without changing their mathematical value.

**Example:**

Original equation:

2x + 3x = 10

Transformed equation:

5x = 10

**Expected result:** Valid transformation.

**Mathematical condition:** The simplified expression must be mathematically equivalent to the original expression.