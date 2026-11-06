import pytest
from sympy import Eq, Symbol
from mathtrace.validator import compare_equations


from mathtrace.parser import (
    validate_equation_format,
    parse_expression,
    parse_equation,
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

def test_parse_complete_equation():
    equation = parse_equation("2*x + 3 = 11")

    assert equation.lhs == 2 * Symbol("x") + 3
    assert equation.rhs == 11

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