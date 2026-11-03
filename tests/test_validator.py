from sympy import symbols, Eq,S
from mathtrace.validator import (get_solution_set,compare_equations,validate_solution_steps)

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