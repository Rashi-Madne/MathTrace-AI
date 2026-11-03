from sympy import solveset, S

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