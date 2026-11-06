
import ast

from sympy import Eq, Symbol


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

        if isinstance(node.op, ast.Div):
            return left_value / right_value

        if isinstance(node.op, ast.Pow):
            return left_value ** right_value

    # Handle unary operations: -x, +x, -5.
    if isinstance(node, ast.UnaryOp):
        value = parse_expression_node(node.operand)

        if isinstance(node.op, ast.USub):
            return -value

        if isinstance(node.op, ast.UAdd):
            return value

    raise ValueError("Unsupported mathematical expression.")


def parse_equation(text):
    """
    Parse both sides of an equation and preserve its equality structure.
    """

    left_text, right_text = validate_equation_format(text)

    left_expression = parse_expression(left_text)
    right_expression = parse_expression(right_text)

    return Eq(left_expression, right_expression, evaluate=False)


def parse_solution_steps(step_texts):
    """
    Parse a list of equation strings into SymPy equations.
    """

    parsed_steps = []

    for step in step_texts:
        equation = parse_equation(step)
        parsed_steps.append(equation)

    return parsed_steps
