from sympy import solveset, S,simplify

def get_solution_set(equation,variable):
    if equation is S.true:
        return S.Reals

    if equation is S.false:
        return S.EmptySet

    return solveset(
        equation.lhs-equation.rhs,variable,domain=S.Reals
    )

def compare_equations(original, transformed, variable):

    original_solutions = get_solution_set(original, variable)

    transformed_solutions = get_solution_set(transformed, variable)

    if original_solutions == transformed_solutions:
        return True
    else:
        return False

def validate_solution_steps(steps,variable):

    if len(steps)<2:
        return{
            "status":"insufficient_steps",
            "message":"At least two equations required"
        }

    for i in range(len(steps)-1):
        original=steps[i]
        transformed=steps[i+1]

        is_valid=compare_equations(original,transformed,variable)

        if not is_valid:
            return {
            "status":"invalid",
            "error_step":i+1,
            "original":str(original),
            "transformed":str(transformed)
        }
    return{
        "status":"valid",
        "message":"All consecutive equation pairs passed the comparision."
    }

def detect_sign_error(original, transformed, variable):

    constant = simplify(original.lhs - variable)

    expected_right = simplify(original.rhs - constant)
    wrong_sign_right = simplify(original.rhs + constant)

    if simplify(transformed.lhs - variable) != 0:
        return None

    if simplify(transformed.rhs - expected_right) == 0:
        return None

    if simplify(transformed.rhs - wrong_sign_right) == 0:
        return "sign_error"

    return None


    constant = simplify(original.lhs - variable)

    expected_right = simplify(original.rhs - constant)
    wrong_sign_right = simplify(original.rhs + constant)

    if simplify(transformed.lhs - variable) != 0:
        return None

    if simplify(transformed.rhs - expected_right) == 0:
        return None

    if simplify(transformed.rhs - wrong_sign_right) == 0:
        return "sign_error"
        error_category = detect_sign_error(
            original, transformed, variable
        )

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
            "corrected_equation": f"{variable} = {simplify(original.rhs - (original.lhs - variable))}"
        }

    return {
        "status": "invalid",
        "error_category": None,
        "explanation": "The transformed equation does not preserve the original solution set.",
        "correction": None,
        "corrected_equation": None
    }