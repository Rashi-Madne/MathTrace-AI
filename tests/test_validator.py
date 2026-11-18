
from sympy import symbols, Eq, S, FiniteSet

from mathtrace.validator import (
    get_solution_set,
    compare_equations,
    validate_solution_steps,
    explain_error
)

from mathtrace.parser import parse_equation


# Create the mathematical variable used throughout these tests.
x = symbols('x')


# --------------------------------------------------
# 1. EQUATION COMPARISON TESTS
# --------------------------------------------------

def test_equivalent_equations():
    original = Eq(2*x + 3, 11)
    transformed = Eq(2*x + 4, 12)

    assert compare_equations(original, transformed, x) == True


def test_different_solution_sets():
    original = Eq(2*x + 3, 11)
    transformed = Eq(2*x + 3, 12)

    assert not compare_equations(original, transformed, x)


def test_equivalent_equations_with_different_forms():
    original = Eq(x, 4)
    transformed = Eq(2*x, 8)

    assert compare_equations(original, transformed, x)


# --------------------------------------------------
# 2. SOLUTION STEP VALIDATION TESTS
# --------------------------------------------------

def test_detects_first_invalid_step():
    steps = [
        Eq(2*x + 3, 11),
        Eq(2*x, 14),
        Eq(x, 7),
        Eq(x, 8)
    ]

    result = validate_solution_steps(steps, x)

    assert result["status"] == "invalid"
    assert result["error_step"] == 1


def test_all_steps_are_valid():
    steps = [
        Eq(2*x + 3, 11),
        Eq(2*x, 8),
        Eq(x, 4)
    ]

    result = validate_solution_steps(steps, x)

    assert result["status"] == "valid"


def test_insufficient_steps():
    steps = [Eq(x, 4)]

    result = validate_solution_steps(steps, x)

    assert result["status"] == "insufficient_steps"


def test_detects_invalid_step_after_valid_transition():
    steps = [
        Eq(2*x + 3, 11),
        Eq(2*x, 8),
        Eq(x, 5)
    ]

    result = validate_solution_steps(steps, x)

    assert result["status"] == "invalid"
    assert result["error_step"] == 2


# --------------------------------------------------
# 3. SOLUTION SET TESTS
# --------------------------------------------------

def test_true_equation_returns_all_real_numbers():
    equation = Eq(2*(x+3), 2*x+6)

    assert get_solution_set(equation, x) == S.Reals


def test_false_equation_returns_empty_set():
    equation = Eq(x+2, x+5)

    assert get_solution_set(equation, x) == S.EmptySet


def test_boolean_true_matches_identity_equation():
    original = Eq(2*(x+3), 2*x+6)
    transformed = Eq(x, x, evaluate=False)

    assert compare_equations(original, transformed, x)


# --------------------------------------------------
# 4. ERROR EXPLANATION TESTS
# --------------------------------------------------

def test_explain_error_for_valid_transition():
    original = Eq(3*x + 6, 15, evaluate=False)
    transformed = Eq(3*x, 9, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["status"] == "valid"
    assert result["error_category"] is None
    assert result["explanation"] == "No mathematical error detected."


def test_explain_error_for_invalid_transition():
    original = Eq(2*x + 3, 11, evaluate=False)
    transformed = Eq(2*x, 14, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["status"] == "invalid"


# --------------------------------------------------
# 5. SIGN ERROR DETECTION TESTS
# --------------------------------------------------

def test_classifies_sign_error():
    original = Eq(x - 4, 10, evaluate=False)
    transformed = Eq(x, 10 - 4, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["status"] == "invalid"
    assert result["error_category"] == "sign_error"
    assert result["corrected_equation"] == "x = 14"


def test_classifies_sign_error_with_different_constant():
    original = Eq(x - 7, 15, evaluate=False)
    transformed = Eq(x, 15 - 7, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["error_category"] == "sign_error"
    assert result["corrected_equation"] == "x = 22"


def test_classifies_sign_error_with_positive_constant():
    original = Eq(x + 3, 12, evaluate=False)
    transformed = Eq(x, 12 + 3, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["error_category"] == "sign_error"
    assert result["corrected_equation"] == "x = 9"


def test_does_not_classify_sign_error_when_coefficient_is_not_one():
    original = Eq(2*x - 4, 10, evaluate=False)
    transformed = Eq(x, 10 + 4, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["status"] == "invalid"
    assert result["error_category"] is None


def test_does_not_classify_symbolic_constant_as_sign_error():
    y = symbols('y')

    original = Eq(x + y, 10, evaluate=False)
    transformed = Eq(x, 10 + y, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["status"] == "invalid"
    assert result["error_category"] is None


def test_does_not_classify_quadratic_expression_as_sign_error():
    original = Eq(x**2 + 4, 10, evaluate=False)
    transformed = Eq(x, 10 - 4, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["status"] == "invalid"
    assert result["error_category"] is None


def test_does_not_classify_variable_dependent_rhs_as_sign_error():
    y = symbols('y')

    original = Eq(x - 4, y + 10, evaluate=False)
    transformed = Eq(x, y + 10 + 4, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["status"] == "valid"
    assert result["error_category"] is None


def test_classifies_sign_error_with_non_unit_coefficient():
    original = parse_equation("2*x + 3 = 11")
    transformed = parse_equation("2*x = 14")

    result = explain_error(original, transformed, x)

    assert result["error_category"] == "sign_error"
    assert result["corrected_equation"] == "2*x = 8"


def test_classifies_sign_error_after_isolating_variable():
    original = parse_equation("2*x + 3 = 11")
    transformed = parse_equation("x = 7")

    result = explain_error(original, transformed, x)

    assert result["error_category"] == "sign_error"
    assert result["corrected_equation"] == "x = 4"


# --------------------------------------------------
# 6. ARITHMETIC ERROR DETECTION TESTS
# --------------------------------------------------

def test_classifies_possible_arithmetic_error():
    original = Eq(2*x, 8, evaluate=False)
    transformed = Eq(x, 5, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["status"] == "invalid"
    assert result["error_category"] == "possible_arithmetic_error"
    assert result["corrected_equation"] == "x = 4"


def test_does_not_classify_wrong_coefficient_as_arithmetic_error():
    original = Eq(2*x, 8, evaluate=False)
    transformed = Eq(3*x, 4, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["status"] == "invalid"
    assert result["error_category"] is None


def test_classifies_arithmetic_error_with_constant():
    original = Eq(2*x + 3, 11, evaluate=False)
    transformed = Eq(x, 5, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["status"] == "invalid"
    assert result["error_category"] == "possible_arithmetic_error"
    assert result["corrected_equation"] == "x = 4"


# --------------------------------------------------
# 7. DOMAIN RESTRICTION TESTS
# --------------------------------------------------

def test_equation_with_variable_denominator_excludes_zero():
    equation = parse_equation("x/x = 1")

    assert get_solution_set(equation, x) == S.Reals - FiniteSet(0)


def test_comparison_respects_variable_denominator_restriction():
    original = parse_equation("x/x = 1")
    transformed = parse_equation("x = 1")

    assert compare_equations(original, transformed, x) is False


def test_equation_with_linear_denominator_excludes_forbidden_value():
    equation = parse_equation("1/(x-2) = 3")

    assert get_solution_set(equation, x) == FiniteSet(S(7) / 3)


def test_nested_denominators_preserve_all_restrictions():
    equation = parse_equation("1/(1/(x-2)) = 3")

    assert get_solution_set(equation, x) == FiniteSet(S(5))
