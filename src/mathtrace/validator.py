from sympy import solveset, S, simplify
from mathtrace.parser import parse_solution_steps


def get_solution_set(equation, variable):
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
    original_solutions = get_solution_set(original, variable)
    transformed_solutions = get_solution_set(transformed, variable)

    if original_solutions == transformed_solutions:
        return True
    else:
        return False


def validate_solution_steps(steps, variable):
    if len(steps) < 2:
        return {
            "status": "insufficient_steps",
            "message": "At least two equations required"
        }

    for i in range(len(steps) - 1):
        original = steps[i]
        transformed = steps[i + 1]

        is_valid = compare_equations(original, transformed, variable)

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
    try:
        parsed_steps = parse_solution_steps(step_texts)

    except (ValueError, TypeError) as error:
        return {
            "status": "invalid_input",
            "message": str(error)
        }

    return validate_solution_steps(parsed_steps, variable)





def detect_sign_error(original, transformed, variable):
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


def explain_error(original, transformed, variable):
    is_valid = compare_equations(original, transformed, variable)

    if is_valid:
        return {
            "status": "valid",
            "error_category": None,
            "explanation": "No mathematical error detected.",
            "correction": None,
            "corrected_equation": None
        }

    error_category = detect_sign_error(
        original, transformed, variable
    )

    if error_category == "sign_error":
        return {
            "status": "invalid",
            "error_category": "sign_error",
            "explanation": "The constant was moved to the other side with the wrong sign.",
            "correction": f"Apply the inverse operation to both sides to isolate {variable}.",
            "corrected_equation": (
                f"{variable} = "
                f"{simplify(original.rhs - (original.lhs - variable))}"
            )
        }

    return {
        "status": "invalid",
        "error_category": None,
        "explanation": "The transformed equation does not preserve the original solution set.",
        "correction": None,
        "corrected_equation": None
    }
