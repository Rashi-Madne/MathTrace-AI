from sympy import symbols, Eq, S
from mathtrace.validator import (
    get_solution_set,
    compare_equations,
    validate_solution_steps,
    explain_error
)

x = symbols('x')


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

def test_true_equation_returns_all_real_numbers():
    equation=Eq(2*(x+3),2*x+6)

    assert get_solution_set(equation,x)==S.Reals

def test_false_equation_returns_empty_set():
    equation=Eq(x+2,x+5)

    assert get_solution_set(equation,x)==S.EmptySet
def test_boolean_true_matches_identity_equation():
    original = Eq(2*(x+3), 2*x+6)
    transformed = Eq(x, x, evaluate=False)

    assert compare_equations(original, transformed, x)

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

def test_classifies_sign_error():

    original = Eq(x - 4, 10, evaluate=False)
    transformed = Eq(x, 10 - 4, evaluate=False)

    result = explain_error(original, transformed, x)

    assert result["status"] == "invalid"
    assert result["error_category"] == "sign_error"
    assert result["corrected_equation"] == "x = 14"

def test_classifies_sign_error_with_different_constant():
    original=Eq(x-7,15,evaluate=False)
    transformed=Eq(x,15-7,evaluate=False)
    result=explain_error(original,transformed,x)

    assert result["error_category"]=="sign_error"
    assert result["corrected_equation"]=="x = 22"

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