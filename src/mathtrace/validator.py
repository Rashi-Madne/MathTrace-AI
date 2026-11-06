
from sympy import solveset, S, simplify
from mathtrace.parser import parse_solution_steps


def get_solution_set(equation, variable):
    """
    Find all real values of the variable that satisfy an equation.
    """

    if equation is S.true:
        return S.Reals

    if equation is S.false:
        return S.EmptySet

    return solveset(
        equation.lhs - equation.rhs,
        variable,
        domain=S.Reals
    )


def compare_equations(original, transformed, variable):
    """
    Check whether two equations have the same solution set.
    """

    original_solutions = get_solution_set(original, variable)
    transformed_solutions = get_solution_set(transformed, variable)

    return original_solutions == transformed_solutions


def validate_solution_steps(steps, variable):
    """
    Validate consecutive equations and identify the first invalid step.
    """

    if len(steps) < 2:
        return {
            "status": "insufficient_steps",
            "message": "At least two equations required"
        }

    for i in range(len(steps) - 1):
        original = steps[i]
        transformed = steps[i + 1]

        is_valid = compare_equations(
            original,
            transformed,
            variable
        )

        if not is_valid:
            return {
                "status": "invalid",
                "error_step": i + 1,
                "original": str(original),
                "transformed": str(transformed)
            }

    return {
        "status": "valid",
        "message": "All consecutive equation pairs passed the comparison."
    }


def validate_text_solution_steps(step_texts, variable):
    """
    Parse text equations, validate them, and attach detailed feedback
    when an incorrect transformation is detected.
    """

    try:
        parsed_steps = parse_solution_steps(step_texts)

    except (ValueError, TypeError) as error:
        return {
            "status": "invalid_input",
            "message": str(error)
        }

    result = validate_solution_steps(parsed_steps, variable)

    if result["status"] == "invalid":

        error_index = result["error_step"] - 1

        original = parsed_steps[error_index]
        transformed = parsed_steps[error_index + 1]

        feedback = explain_error(
            original,
            transformed,
            variable
        )

        result.update(feedback)

    return result


def detect_sign_error(original, transformed, variable):
    """
    Detect a specific sign error when moving a constant
    across the equality sign in a supported linear equation.
    """

    coefficient = simplify(original.lhs.coeff(variable))

    if coefficient != 1:
        return None

    if original.lhs.diff(variable, 2) != 0:
        return None

    constant = simplify(original.lhs - variable)

    if not constant.is_number:
        return None

    if not original.rhs.is_number:
        return None

    expected_right = simplify(original.rhs - constant)
    wrong_sign_right = simplify(original.rhs + constant)

    if simplify(transformed.lhs - variable) != 0:
        return None

    if simplify(transformed.rhs - expected_right) == 0:
        return None

    if simplify(transformed.rhs - wrong_sign_right) == 0:
        return "sign_error"

    return None



def detect_arithmetic_error(original, transformed, variable):
    """
    Detect a possible arithmetic error when isolating a variable
    in a supported linear equation.
    """

    coefficient = simplify(original.lhs.coeff(variable))

    if coefficient != 1:
        return None

    if original.lhs.diff(variable, 2) != 0:
        return None

    constant = simplify(original.lhs - variable)

    if not constant.is_number or constant == 0:
        return None

    if not original.rhs.is_number:
        return None

    if simplify(transformed.lhs - variable) != 0:
        return None

    expected_right = simplify(original.rhs - constant)
    wrong_sign_right = simplify(original.rhs + constant)

    if simplify(transformed.rhs - expected_right) == 0:
        return None

    if simplify(transformed.rhs - wrong_sign_right) == 0:
        return None

    return "possible_arithmetic_error"


def explain_error(original, transformed, variable):
    """
    Generate an explanation and correction for an invalid transformation.
    """

    is_valid = compare_equations(
        original,
        transformed,
        variable
    )

    if is_valid:
        return {
            "status": "valid",
            "error_category": None,
            "explanation": "No mathematical error detected.",
            "correction": None,
            "corrected_equation": None
        }

    error_category = detect_sign_error(
        original,
        transformed,
        variable
    )

    if error_category == "sign_error":
        return {
            "status": "invalid",
            "error_category": "sign_error",
            "explanation": (
                "The constant was moved to the other side "
                "with the wrong sign."
            ),
            "correction": (
                f"Apply the inverse operation to both sides "
                f"to isolate {variable}."
            ),
            "corrected_equation": (
                f"{variable} = "
                f"{simplify(original.rhs - (original.lhs - variable))}"
            )
        }


    arithmetic_error = detect_arithmetic_error(
        original,
        transformed,
        variable
    )

    if arithmetic_error == "possible_arithmetic_error":

        constant = simplify(original.lhs - variable)
        expected_right = simplify(original.rhs - constant)

        return {
            "status": "invalid",
            "error_category": "possible_arithmetic_error",
            "explanation": (
                "The operation appears to be appropriate, "
                "but the arithmetic result may be incorrect."
            ),
            "correction": (
                f"Recheck the inverse-operation calculation: "
                f"{original.rhs} - ({constant}) = {expected_right}."
            ),
            "corrected_equation": (
                f"{variable} = {expected_right}"
            )
        }


    return {
        "status": "invalid",
        "error_category": None,
        "explanation": (
            "The transformed equation does not preserve "
            "the original solution set."
        ),
        "correction": None,
        "corrected_equation": None
    }
