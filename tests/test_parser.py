
import pytest
from sympy import Symbol, Rational

from mathtrace.parser import (
    validate_equation_format,
    parse_expression,
    parse_equation,
    parse_solution_steps,
)

from mathtrace.validator import (
    compare_equations,
    validate_text_solution_steps,
)

def test_valid_equation_format():
    result = validate_equation_format("2*x + 3 = 11")

    assert result == ("2*x + 3", "11")


def test_equation_with_extra_spaces():
    result = validate_equation_format("  2*x + 3  =  11  ")

    assert result == ("2*x + 3", "11")


def test_empty_equation_is_rejected():
    with pytest.raises(ValueError):
        validate_equation_format("")


def test_equation_without_equal_sign_is_rejected():
    with pytest.raises(ValueError):
        validate_equation_format("2*x + 3")


def test_equation_with_multiple_equal_signs_is_rejected():
    with pytest.raises(ValueError):
        validate_equation_format("x + 2 = 5 = 7")


def test_equation_with_missing_left_side_is_rejected():
    with pytest.raises(ValueError):
        validate_equation_format(" = 5")


def test_equation_with_missing_right_side_is_rejected():
    with pytest.raises(ValueError):
        validate_equation_format("x + 2 = ")

def test_parse_expression_rejects_non_string_input():
    with pytest.raises(TypeError, match="Expression input must be text"):
        parse_expression(123)

def test_validate_equation_format_rejects_non_string_input():
    with pytest.raises(TypeError, match="Equation input must be text"):
        validate_equation_format(123)

def test_parse_solution_steps_rejects_empty_input():
    with pytest.raises(ValueError, match="At least one solution step is required"):
        parse_solution_steps([])

def test_parse_solution_steps_rejects_non_list_input():
    with pytest.raises(TypeError, match="Solution steps must be provided as a list"):
        parse_solution_steps("2*x = 4")

def test_parse_solution_steps_rejects_non_string_step():
    steps = [
        "2*x + 3 = 11",
        123,
        "x = 4"
    ]

    with pytest.raises(TypeError, match="Equation input must be text"):
        parse_solution_steps(steps)

def test_parse_solution_steps_rejects_empty_step():
    steps = [
        "2*x + 3 = 11",
        "",
        "x = 4"
    ]

    with pytest.raises(ValueError, match="Equation input cannot be empty"):
        parse_solution_steps(steps)


def test_parse_integer():
    assert parse_expression("5") == 5


def test_parse_variable():
    assert parse_expression("x") == Symbol("x")


def test_parse_addition():
    assert parse_expression("x + 5") == Symbol("x") + 5


def test_parse_subtraction():
    assert parse_expression("x - 3") == Symbol("x") - 3


def test_parse_multiplication():
    assert parse_expression("2*x") == 2 * Symbol("x")


def test_parse_division():
    assert parse_expression("x / 2") == Symbol("x") / 2

def test_parse_integer_fraction_exactly():
    assert parse_expression("2/3") == Rational(2, 3)


def test_parse_fraction_addition_exactly():
    assert parse_expression("1/2 + 1/3") == Rational(5, 6)

def test_parse_exponentiation():
    assert parse_expression("x**2") == Symbol("x")**2


def test_parse_negative_number():
    assert parse_expression("-5") == -5


def test_parse_negative_variable():
    assert parse_expression("-x") == -Symbol("x")


def test_parse_expression_with_brackets():
    assert parse_expression("2*(x + 3)") == 2 * (Symbol("x") + 3)


def test_parse_complete_equation():
    equation = parse_equation("2*x + 3 = 11")

    assert equation.lhs == 2 * Symbol("x") + 3
    assert equation.rhs == 11


def test_parse_multiple_solution_steps():
    steps = [
        "2*x + 3 = 11",
        "2*x = 8",
        "x = 4",
    ]

    parsed_steps = parse_solution_steps(steps)

    assert len(parsed_steps) == 3
    assert parsed_steps[0].lhs == 2 * Symbol("x") + 3
    assert parsed_steps[1].lhs == 2 * Symbol("x")
    assert parsed_steps[2].lhs == Symbol("x")

def test_invalid_expression_is_rejected():
    with pytest.raises(ValueError):
        parse_expression("2*x +")


def test_unsupported_variable_is_rejected():
    with pytest.raises(ValueError):
        parse_expression("y + 5")


def test_unsupported_function_call_is_rejected():
    with pytest.raises(ValueError):
        parse_expression("sin(x)")


def test_unsupported_operator_is_rejected():
    with pytest.raises(ValueError):
        parse_expression("x // 2")


def test_parsed_equations_can_be_compared():
    original = parse_equation("2*x + 3 = 11")
    transformed = parse_equation("2*x = 8")

    assert compare_equations(original, transformed, Symbol("x"))


def test_parsed_equations_detect_incorrect_transformation():
    original = parse_equation("2*x + 3 = 11")
    transformed = parse_equation("2*x = 10")

    assert not compare_equations(original, transformed, Symbol("x"))


def test_text_solution_steps_accepts_valid_work():
    steps = [
        "2*x + 3 = 11",
        "2*x = 8",
        "x = 4",
    ]

    result = validate_text_solution_steps(steps, Symbol("x"))

    assert result["status"] == "valid"


def test_text_solution_steps_detects_incorrect_work():
    steps = [
        "2*x + 3 = 11",
        "2*x = 10",
        "x = 5",
    ]

    result = validate_text_solution_steps(steps, Symbol("x"))

    assert result["status"] == "invalid"
    assert result["error_step"] == 1


def test_text_solution_steps_handles_invalid_input():
    steps = [
        "2*x + 3 = 11",
        "2*x + = 8",
    ]

    result = validate_text_solution_steps(steps, Symbol("x"))

    assert result["status"] == "invalid_input"
    assert "message" in result


def test_text_solution_steps_returns_sign_error_feedback():
    steps = [
        "x + 3 = 11",
        "x = 14",
    ]

    result = validate_text_solution_steps(steps, Symbol("x"))

    assert result["status"] == "invalid"
    assert result["error_step"] == 1
    assert result["error_category"] == "sign_error"

    assert result["explanation"] == (
        "The constant was moved to the other side "
        "with the wrong sign."
    )

    assert result["corrected_equation"] == "x = 8"


def test_text_solution_steps_detects_possible_arithmetic_error():
    steps = [
        "x + 3 = 11",
        "x = 9",
    ]

    result = validate_text_solution_steps(steps, Symbol("x"))

    assert result["status"] == "invalid"
    assert result["error_step"] == 1
    assert result["error_category"] == "possible_arithmetic_error"
    assert result["corrected_equation"] == "x = 8"

    assert "arithmetic result may be incorrect" in result["explanation"]


def test_text_solution_steps_detects_arithmetic_error_with_coefficient():
    steps = [
        "2*x + 3 = 11",
        "2*x = 8",
        "x = 18",
    ]

    result = validate_text_solution_steps(steps, Symbol("x"))

    assert result["status"] == "invalid"
    assert result["error_step"] == 2
    assert result["error_category"] == "possible_arithmetic_error"
    assert result["corrected_equation"] == "x = 4"


def test_parse_division_by_zero():
    with pytest.raises(ValueError):
        parse_expression("1/0")

def test_parse_symbolic_division_by_zero():
    with pytest.raises(ValueError):
        parse_expression("x/0")

def test_parse_division_by_expression_that_simplifies_to_zero():
    with pytest.raises(ValueError):
        parse_expression("x/(1-1)")


def test_parse_zero_raised_to_negative_power():
    with pytest.raises(ValueError):
        parse_expression("0**-1")


def test_parse_100_positive_terms():
    expression = " + ".join(
        f"{i}*x" for i in range(1, 101)
    )

    assert parse_expression(expression) == 5050 * Symbol("x")


def test_parse_100_alternating_sign_terms():
    expression = " + ".join(
        f"{i}*x" if i % 2 == 1 else f"-{i}*x"
        for i in range(1, 101)
    )

    assert parse_expression(expression) == -50 * Symbol("x")


def test_parse_100_variable_and_constant_terms():
    expression = " + ".join(
        f"{i}*x + {i}" for i in range(1, 101)
    )

    assert parse_expression(expression) == (
        5050 * Symbol("x") + 5050
    )
