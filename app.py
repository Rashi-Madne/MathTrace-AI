
import streamlit as st
from sympy import Symbol
from mathtrace.validator import validate_text_solution_steps


# Configure the web application
st.set_page_config(
    page_title="MathTrace AI",
    page_icon="📐",
    layout="centered"
)


# Application heading
st.title("📐 MathTrace AI")

st.subheader("AI-Assisted Algebra Step Checker")

st.write(
    "Enter your algebra solution steps, one equation per line. "
    "MathTrace AI checks mathematical transformations, "
    "identifies supported errors, and provides corrective feedback."
)


# Section for entering mathematical solutions
st.header("Check Your Solution")

st.write(
    "Enter each mathematical step on a separate line."
)

solution_text = st.text_area(
    "Your solution steps",
    placeholder="x + 3 = 11\nx = 8",
    height=180
)


# Check the solution when the button is clicked
if st.button("Check Solution", type="primary"):

    step_texts = [
        line.strip()
        for line in solution_text.splitlines()
        if line.strip()
    ]

    if len(step_texts) < 2:
        st.warning("Please enter at least two solution steps.")

    else:
        result = validate_text_solution_steps(
            step_texts,
            Symbol("x")
        )

        if result["status"] == "valid":
            st.success("Excellent! All solution steps are valid.")

        elif result["status"] == "invalid":
            st.error(
                f"Incorrect transformation at step "
                f"{result['error_step']}."
            )

            st.write("**Your original equation:**")
            st.write(step_texts[result["error_step"] - 1])

            st.write("**Your transformed equation:**")
            st.write(step_texts[result["error_step"]])

            st.write("**Explanation:**")
            st.write(result.get("explanation"))

            if result.get("corrected_equation"):
                st.info(
                    f"Suggested correction: "
                    f"{result['corrected_equation']}"
                )

        else:
            st.warning(
                result.get("message", "Unable to validate the solution.")
            )
