
import ast
from dataclasses import dataclass
import sympy
from sympy import Eq, Symbol

@dataclass
class ParsedEquation:
    equation: object
    restrictions: list

    @property
    def lhs(self):
        return self.equation.lhs

    @property
    def rhs(self):
        return self.equation.rhs

def validate_equation_format(text):
    """
    Check whether the input has the basic structure of an equation.
    """

    if not isinstance(text, str):
        raise TypeError("Equation input must be text.")

    text = text.strip()

    if not text:
        raise ValueError("Equation input cannot be empty.")

    if text.count("=") != 1:
        raise ValueError("An equation must contain exactly one '=' sign.")

    left_text, right_text = text.split("=")

    left_text = left_text.strip()
    right_text = right_text.strip()

    if not left_text or not right_text:
        raise ValueError(
            "Both sides of the equation must contain an expression."
        )

    return left_text, right_text


def parse_expression(expression):
    """
    Safely convert a supported mathematical expression into a SymPy expression.
    """

    if not isinstance(expression, str):
        raise TypeError("Expression input must be text.")

    try:
        parsed_expression = ast.parse(expression, mode="eval")
    except SyntaxError:
        raise ValueError("Invalid mathematical expression.")

    return parse_expression_node(parsed_expression.body)


def parse_expression_node(node):
    """
    Recursively process the allowed nodes in Python's Abstract Syntax Tree.
    """

    # Handle numeric constants.
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)) and not isinstance(
            node.value, bool
        ):
            return node.value

        raise ValueError("Only numeric constants are allowed.")

    # Handle the supported variable.

    if isinstance(node, ast.Name):
        if node.id == "x":
            return Symbol("x")

        raise ValueError("Only the variable 'x' is supported.")

    # Handle binary operations: +, -, *, /, **.
    if isinstance(node, ast.BinOp):
        left_value = parse_expression_node(node.left)
        right_value = parse_expression_node(node.right)

        if isinstance(node.op, ast.Add):
            return left_value + right_value

        if isinstance(node.op, ast.Sub):
            return left_value - right_value

        if isinstance(node.op, ast.Mult):
            return left_value * right_value

        # Handle division and prevent division by zero.
        if isinstance(node.op, ast.Div):
            if right_value == 0:
                raise ValueError("Division by zero is not allowed.")

            if isinstance(left_value, int) and isinstance(right_value, int):
                return sympy.Rational(left_value, right_value)

            return left_value / right_value

        # Handle exponentiation and prevent zero raised to a negative power.
        if isinstance(node.op, ast.Pow):
            if (
                left_value == 0
                and isinstance(right_value, (int, float))
                and right_value < 0
            ):
                raise ValueError(
                    "Zero cannot be raised to a negative power."
                )

            return left_value ** right_value

    # Handle unary operations: -x, +x, -5.
    if isinstance(node, ast.UnaryOp):
        value = parse_expression_node(node.operand)

        if isinstance(node.op, ast.USub):
            return -value

        if isinstance(node.op, ast.UAdd):
            return value

    raise ValueError("Unsupported mathematical expression.")

def collect_denominator_restrictions(node):
    """
    Collect denominator expressions that must not equal zero.
    """

    restrictions = []

    if isinstance(node, ast.BinOp):

        if isinstance(node.op, ast.Div):
            denominator = parse_expression_node(node.right)
            restrictions.append(denominator)

        for child in ast.iter_child_nodes(node):
            restrictions.extend(
                collect_denominator_restrictions(child)
            )

    return restrictions

def parse_equation(text):
    """
    Parse both sides of an equation and preserve its equality structure.
    """

    left_text, right_text = validate_equation_format(text)

    try:
        left_ast = ast.parse(left_text, mode="eval").body
        right_ast = ast.parse(right_text, mode="eval").body

    except SyntaxError:
        raise ValueError("Invalid mathematical expression.")

    restrictions = (
        collect_denominator_restrictions(left_ast)
        + collect_denominator_restrictions(right_ast)
    )

    left_expression = parse_expression_node(left_ast)
    right_expression = parse_expression_node(right_ast)

    equation = Eq(
        left_expression,
        right_expression,
        evaluate=False
    )

    return ParsedEquation(
        equation=equation,
        restrictions=restrictions
    )


def parse_solution_steps(step_texts):
    """
    Parse a list of equation strings into SymPy equations.
    """

    if not isinstance(step_texts, list):
        raise TypeError(
            "Solution steps must be provided as a list."
        )

    if not step_texts:
        raise ValueError("At least one solution step is required.")

    parsed_steps = []

    for step in step_texts:
        equation = parse_equation(step)
        parsed_steps.append(equation)

    return parsed_steps
