from sympy import solve

def compare_equations(original,transformed):
    original_solutions=solve(original)
    transformed_solutions=solve(transformed)

    if original_solutions==transformed_solutions:
        return True
    else:
        return False

def validate_solution_steps(steps):

    if len(steps)<2:
        return{
            "status":"insufficient_steps",
            "message":"At least two equations required"
        }

    for i in range(len(steps)-1):
        original=steps[i]
        transformed=steps[i+1]

        is_valid=compare_equations(original,transformed)

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