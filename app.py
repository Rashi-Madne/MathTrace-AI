
import streamlit as st
from sympy import Symbol

from mathtrace.validator import validate_text_solution_steps


# ==================================================
# 1. PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="MathTrace AI | Mathematical Reasoning",
    page_icon="∑",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==================================================
# 2. GRAPHITE & SUBTLE SAGE DESIGN SYSTEM
# ==================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap');

    :root {
        --bg: #1D2229;
        --surface: #292F37;
        --surface-2: #333B45;
        --surface-3: #242A32;

        --text: #F5F5F1;
        --muted: #C3C9C8;
        --border: #414B55;

        --accent: #A8C9B1;
        --accent-soft: #34453B;

        --blue: #8194A8;
        --blue-soft: #303D4A;

        --success: #A8C9B1;
        --success-bg: #263A31;

        --error: #E69A9A;
        --error-bg: #402E33;

        --warning: #E5C38A;
        --warning-bg: #40382B;
    }

    /* GLOBAL */

    html,
    body,
    [class*="css"],
    .stApp,
    .stApp * {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: var(--bg);
        color: var(--text);
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2.8rem;
        padding-bottom: 4rem;
        padding-left: 3.5rem;
        padding-right: 3.5rem;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stDecoration"] {
        display: none;
    }

    /* HEADINGS */

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif !important;
        color: var(--text) !important;
        letter-spacing: -0.5px;
    }

    h1 {
        font-weight: 700 !important;
    }

    h2 {
        font-size: 2rem !important;
        font-weight: 700 !important;
    }

    h3 {
        font-size: 1.35rem !important;
        font-weight: 700 !important;
    }

    p, label, li {
        font-family: 'Inter', sans-serif;
        color: var(--muted);
        font-size: 0.98rem;
        line-height: 1.8;
    }

    [data-testid="stMarkdownContainer"] p {
        line-height: 1.8;
    }

    /* BRAND */

    .brand {
        font-family: 'Poppins', sans-serif;
        font-size: 2.1rem;
        font-weight: 700;
        letter-spacing: -1.2px;
        color: var(--text);
    }

    .brand span {
        color: var(--accent);
    }

    .eyebrow,
    .section-label {
        color: var(--accent);
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 1.8px;
        text-transform: uppercase;
    }

    .status-pill {
        display: inline-block;
        background: var(--accent-soft);
        color: #C9E0CF;
        border: 1px solid #627D69;
        border-radius: 6px;
        padding: 8px 13px;
        font-family: 'Inter', sans-serif;
        font-size: 0.73rem;
        font-weight: 700;
        letter-spacing: 0.7px;
    }

    /* HERO */

    .hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: clamp(2.8rem, 5vw, 4.5rem);
        line-height: 1.2;
        font-weight: 700;
        letter-spacing: -2px;
        color: var(--text);
        margin: 20px 0;
    }

    .gradient-text {
        color: var(--accent);
        -webkit-text-fill-color: var(--accent);
    }

    .hero-description {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        font-weight: 500;
        line-height: 1.9;
        color: var(--muted);
        max-width: 790px;
    }

    /* GENERAL SPACING */

    hr {
        border: none;
        border-top: 1px solid var(--border);
        margin-top: 2.5rem;
        margin-bottom: 2.5rem;
    }

    /* CARDS */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 11px;
        padding: 1.5rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }

    /* METRICS */

    [data-testid="stMetric"] {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 24px;
        min-height: 120px;
    }

    [data-testid="stMetricLabel"] {
        color: var(--muted) !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.92rem !important;
        font-weight: 600 !important;
    }

    [data-testid="stMetricValue"] {
        color: var(--text) !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
    }

    /* MATHEMATICAL INPUT */

    .stTextArea textarea {
        background: var(--surface-3) !important;
        color: var(--text) !important;
        border: 1px solid #56616B !important;
        border-radius: 9px !important;
        padding: 20px !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 1rem !important;
        line-height: 2 !important;
        min-height: 220px;
    }

    .stTextArea textarea:focus {
        border: 1px solid var(--accent) !important;
        box-shadow: 0 0 0 3px #A8C9B125 !important;
    }

    .stTextArea textarea::placeholder {
        color: #929DA4 !important;
    }

    /* BUTTONS */

    .stButton button,
    [data-testid="stFormSubmitButton"] button {
        min-height: 46px;
        border-radius: 8px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.96rem !important;
        font-weight: 700 !important;
        transition: all 0.2s ease;
    }

    .stButton button {
        background: var(--surface-2);
        color: var(--text);
        border: 1px solid var(--border);
    }

    .stButton button:hover {
        background: #3D4851;
        border-color: var(--accent);
        color: #D3E6D7;
    }

    [data-testid="stFormSubmitButton"] button {
        background: #A8C9B1 !important;
        color: #202B25 !important;
        border: 1px solid #A8C9B1 !important;
        font-weight: 700 !important;
    }

    [data-testid="stFormSubmitButton"] button *,
    [data-testid="stFormSubmitButton"] button p,
    [data-testid="stFormSubmitButton"] button span {
        color: #202B25 !important;
        -webkit-text-fill-color: #202B25 !important;
    }

    [data-testid="stFormSubmitButton"] button:hover {
        background: #BDD9C4 !important;
        border-color: #BDD9C4 !important;
        color: #1D2922 !important;
    }

    /* RESULT PANELS */

    .success-panel {
        background: var(--success-bg);
        border: 1px solid #56765F;
        border-left: 4px solid var(--success);
        border-radius: 8px;
        padding: 23px 26px;
        color: #D5E8D9;
        line-height: 1.9;
    }

    .error-panel {
        background: var(--error-bg);
        border: 1px solid #80505A;
        border-left: 4px solid var(--error);
        border-radius: 8px;
        padding: 23px 26px;
        color: #F5D9DC;
        line-height: 1.9;
    }

    .info-panel {
        background: var(--blue-soft);
        border: 1px solid #526477;
        border-radius: 8px;
        padding: 23px 26px;
        color: #D8E0E8;
    }

    /* TIMELINE */

    .trace-number {
        color: var(--accent);
        font-family: 'Inter', sans-serif;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .trace-equation {
        color: var(--text);
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 1.15rem;
        font-weight: 500;
    }

    .muted {
        color: var(--muted);
        font-family: 'Inter', sans-serif;
        font-size: 0.94rem;
        line-height: 1.8;
    }

    /* CODE */

    code,
    pre,
    [data-testid="stCode"] *,
    .stTextArea textarea {
        font-family: 'JetBrains Mono', monospace !important;
    }

    [data-testid="stCode"] {
        border-radius: 8px;
    }

    /* TABLES */

    [data-testid="stTable"] {
        background: var(--surface);
        color: var(--text);
    }

    /* ALERTS */

    [data-testid="stAlert"] {
        border-radius: 8px;
        padding: 16px 19px;
    }

    /* PROGRESS */

    [data-testid="stProgressBar"] > div {
        background: #3A4149;
        border-radius: 20px;
    }

    [data-testid="stProgressBar"] > div > div {
        background: var(--accent);
        border-radius: 20px;
    }

    /* FOOTER */

    .footer {
        text-align: center;
        color: #A5AFB1;
        font-family: 'Inter', sans-serif;
        font-size: 0.86rem;
        font-weight: 600;
        line-height: 2;
        padding-top: 30px;
        letter-spacing: 0.5px;
    }

    /* RESPONSIVE */

    @media (max-width: 900px) {
        .block-container {
            padding-left: 1.5rem;
            padding-right: 1.5rem;
            padding-top: 2rem;
        }

        .hero-title {
            font-size: 2.8rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# 3. EXAMPLE SOLUTIONS
# ==================================================

EXAMPLES = {
    "Correct solution": (
        "2*x + 3 = 11\n"
        "2*x = 8\n"
        "x = 4"
    ),

    "Sign error": (
        "2*x + 3 = 11\n"
        "2*x = 14"
    ),

    "Arithmetic error": (
        "2*x + 3 = 11\n"
        "2*x = 8\n"
        "x = 5"
    ),

    "Wrong coefficient": (
        "2*x = 8\n"
        "3*x = 4"
    ),

    "Division by zero": (
        "x/0 = 5"
    )
}


# ==================================================
# 4. SESSION STATE
# ==================================================

if "solution_input" not in st.session_state:
    st.session_state.solution_input = EXAMPLES["Correct solution"]

if "validation_result" not in st.session_state:
    st.session_state.validation_result = None

if "validated_text" not in st.session_state:
    st.session_state.validated_text = None


def load_example(name):
    st.session_state.solution_input = EXAMPLES[name]
    st.session_state.validation_result = None
    st.session_state.validated_text = None


# ==================================================
# 5. HEADER
# ==================================================

header_left, header_right = st.columns([3, 1])

with header_left:

    st.markdown(
        '<div class="brand">∑ MathTrace<span> AI</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="muted">MATHEMATICAL REASONING ENGINE</div>',
        unsafe_allow_html=True
    )

with header_right:

    st.markdown(
        """
        <div style="text-align:right; padding-top:10px;">
            <span class="status-pill">● RESEARCH PROTOTYPE</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()


# ==================================================
# 6. FULL-WIDTH HERO SECTION
# ==================================================

st.markdown(
    '<div class="eyebrow">INTELLIGENT MATHEMATICS LEARNING</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-title">
        Understand every step.<br>
        <span class="gradient-text">Not just the answer.</span>
    </div>

    <div class="hero-description">
        An interactive mathematical reasoning tool that examines
        your working, identifies the first incorrect transition,
        and helps you understand what went wrong.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")


# ==================================================
# 7. FULL-WIDTH SOLUTION WORKSPACE
# ==================================================

st.markdown(
    '<div class="section-label">01 / SOLUTION WORKSPACE</div>',
    unsafe_allow_html=True
)

st.subheader("Enter your working")

st.markdown(
    "Write one equation per line. Use `*` for multiplication "
    "and `**` for powers."
)

st.write("")

st.markdown("**Try a sample problem**")

sample_columns = st.columns(3)

with sample_columns[0]:

    if st.button("✓ Correct", use_container_width=True):
        load_example("Correct solution")
        st.rerun()

with sample_columns[1]:

    if st.button("↗ Sign error", use_container_width=True):
        load_example("Sign error")
        st.rerun()

with sample_columns[2]:

    if st.button("∑ Arithmetic", use_container_width=True):
        load_example("Arithmetic error")
        st.rerun()

with st.form("solution_form"):

    solution_text = st.text_area(
        "Your mathematical solution",
        key="solution_input",
        height=260,
        placeholder=(
            "Example:\n"
            "2*x + 3 = 11\n"
            "2*x = 8\n"
            "x = 4"
        )
    )

    submitted = st.form_submit_button(
        "Analyse my solution  →",
        type="primary",
        use_container_width=True
    )

clear_column, empty_column = st.columns([1, 5])

with clear_column:

    if st.button("Clear workspace", use_container_width=True):

        st.session_state.solution_input = ""
        st.session_state.validation_result = None
        st.session_state.validated_text = None

        st.rerun()


# ==================================================
# 8. HOW MATHTRACE WORKS
# ==================================================

st.write("")
st.divider()

st.markdown(
    '<div class="section-label">02 / QUICK GUIDE</div>',
    unsafe_allow_html=True
)

st.subheader("How MathTrace works")

guide_columns = st.columns(3, gap="large")

guide_steps = [
    (
        "01",
        "Enter equations",
        "Write each mathematical step on a separate line."
    ),
    (
        "02",
        "Analyse transformations",
        "The validator examines consecutive equation transitions."
    ),
    (
        "03",
        "Understand the result",
        "Review the first detected error, its explanation and the suggested correction."
    )
]

for column, (number, heading, description) in zip(
    guide_columns,
    guide_steps
):

    with column:

        with st.container(border=True):

            st.markdown(
                f"""
                <div style="
                    color:#A8C9B1;
                    font-size:0.82rem;
                    font-weight:700;
                    letter-spacing:1.5px;
                    margin-bottom:12px;
                ">
                    STEP {number}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(f"### {heading}")

            st.markdown(
                f'<div class="muted">{description}</div>',
                unsafe_allow_html=True
            )


# ==================================================
# 9. SUPPORTED NOTATION
# ==================================================

st.write("")

with st.container(border=True):

    notation_left, notation_right = st.columns(
        [1, 2],
        gap="large"
    )

    with notation_left:

        st.markdown("### Supported notation")

        st.caption(
            "Current prototype supports typed algebraic "
            "equations using one variable: x."
        )

    with notation_right:

        st.markdown(
            """
            | Operation | Notation |
            |---|---|
            | Multiplication | `2*x` |
            | Power | `x**2` |
            | Division | `x/2` |
            | Brackets | `(x+2)` |
            | Equality | `=` |
            """
        )


# ==================================================
# 10. RUN VALIDATION
# ==================================================

if submitted:

    step_texts = [
        line.strip()
        for line in solution_text.splitlines()
        if line.strip()
    ]

    if not step_texts:

        st.warning(
            "Please enter at least one mathematical equation."
        )

    else:

        try:

            result = validate_text_solution_steps(
                step_texts,
                Symbol("x")
            )

            st.session_state.validation_result = result
            st.session_state.validated_text = solution_text

        except Exception as error:

            st.session_state.validation_result = {
                "status": "invalid_input",
                "message": str(error)
            }

            st.session_state.validated_text = solution_text


# ==================================================
# 11. DISPLAY VALIDATION REPORT
# ==================================================

result = st.session_state.validation_result

if result is not None:

    st.divider()

    st.markdown(
        '<div class="section-label">03 / ANALYSIS REPORT</div>',
        unsafe_allow_html=True
    )

    st.subheader("Your solution analysis")

    if st.session_state.validated_text != st.session_state.solution_input:

        st.info(
            "Your input has changed. Analyse it again "
            "to refresh the report."
        )

    elif result.get("status") == "invalid_input":

        st.error("The input could not be processed.")

        st.write(
            result.get(
                "message",
                "Please check your mathematical notation and try again."
            )
        )

    else:

        step_texts = [
            line.strip()
            for line in st.session_state.validated_text.splitlines()
            if line.strip()
        ]

        total_steps = len(step_texts)
        total_transitions = max(total_steps - 1, 0)

        status = result.get("status")
        error_step = result.get("error_step")
        error_category = result.get("error_category")

        # CALCULATE METRICS

        if status == "valid":

            passed_transitions = total_transitions

        elif status == "invalid" and error_step is not None:

            passed_transitions = max(error_step - 1, 0)

        else:

            passed_transitions = 0

        # METRIC CARDS

        metric1, metric2, metric3 = st.columns(3)

        with metric1:

            st.metric(
                "Equations entered",
                total_steps
            )

        with metric2:

            st.metric(
                "Transitions checked",
                total_transitions
            )

        with metric3:

            st.metric(
                "Validation result",
                "PASSED" if status == "valid" else "REVIEW"
            )

        # VALIDATION STATUS

        if status == "valid":

            st.markdown(
                """
                <div class="success-panel">
                    <strong>✓ All solution steps passed validation.</strong>
                    <br>
                    The mathematical transitions in this solution
                    are consistent with the validator's checks.
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(1.0)

        elif status == "invalid":

            st.markdown(
                """
                <div class="error-panel">
                    <strong>⚠ An incorrect transition was detected.</strong>
                    <br>
                    Review the first flagged step below and compare
                    it with the suggested correction.
                </div>
                """,
                unsafe_allow_html=True
            )

            progress = (
                passed_transitions / total_transitions
                if total_transitions > 0
                else 0.0
            )

            st.progress(
                min(max(progress, 0.0), 1.0)
            )

        # SOLUTION JOURNEY

        st.write("")

        st.markdown("### Solution journey")

        st.caption(
            "Follow the mathematical transformations. "
            "The first incorrect transition is highlighted."
        )

        for index, equation in enumerate(step_texts):

            step_number = index + 1

            is_start = index == 0

            is_error = (
                status == "invalid"
                and error_step is not None
                and not is_start
                and error_step == index
            )

            is_passed = (
                status == "valid"
                or (
                    status == "invalid"
                    and error_step is not None
                    and not is_start
                    and index < error_step
                )
            )

            if is_start:

                icon = "◎"
                status_label = "STARTING POINT"
                status_color = "#8194A8"

            elif is_error:

                icon = "✕"
                status_label = "FIRST INCORRECT STEP"
                status_color = "#E69A9A"

            elif is_passed:

                icon = "✓"
                status_label = "ACCEPTED"
                status_color = "#A8C9B1"

            else:

                icon = "○"
                status_label = "NOT YET VERIFIED"
                status_color = "#AAB5BB"

            with st.container(border=True):

                left, right = st.columns([0.12, 0.88])

                with left:

                    st.markdown(
                        f"""
                        <div style="
                            font-size:27px;
                            font-weight:700;
                            color:{status_color};
                            padding-top:8px;
                            text-align:center;
                        ">
                            {icon}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with right:

                    st.markdown(
                        f"""
                        <div style="
                            color:{status_color};
                            font-size:11px;
                            font-weight:700;
                            letter-spacing:1.3px;
                        ">
                            STEP {step_number:02d} · {status_label}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"### `{equation}`"
                    )

                    if is_start:

                        st.caption(
                            "Your original equation — "
                            "the starting point of the solution."
                        )

                    elif is_error:

                        st.error(
                            "This equation does not follow "
                            "correctly from the previous step."
                        )

                    elif is_passed:

                        st.caption(
                            "This part of the solution passed validation."
                        )

                    else:

                        st.caption(
                            "This step comes after the first "
                            "incorrect transition."
                        )

            # TIMELINE CONNECTOR

            if index < total_steps - 1:

                next_is_error = (
                    status == "invalid"
                    and error_step is not None
                    and error_step == index + 1
                )

                if next_is_error:

                    st.markdown(
                        """
                        <div style="
                            margin-left:34px;
                            padding:10px 15px;
                            border-left:3px solid #E69A9A;
                            color:#E69A9A;
                            font-size:12px;
                            font-weight:700;
                            letter-spacing:1px;
                        ">
                            ↓ &nbsp; INCORRECT TRANSFORMATION
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                else:

                    st.markdown(
                        """
                        <div style="
                            margin-left:34px;
                            padding:10px 15px;
                            border-left:3px solid #8194A8;
                            color:#AAB5BB;
                            font-size:12px;
                            font-weight:700;
                            letter-spacing:1px;
                        ">
                            ↓ &nbsp; NEXT TRANSFORMATION
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        # ERROR ANALYSIS

        if status == "invalid":

            st.write("")

            # EQUATION COMPARISON

            st.markdown("### Equation comparison")

            st.caption(
                "Compare your original transformation "
                "with the suggested corrected equation."
            )

            if error_step is not None:

                previous_index = error_step - 1
                incorrect_index = error_step

                if (
                    0 <= previous_index < len(step_texts)
                    and 0 <= incorrect_index < len(step_texts)
                ):

                    student_equation = step_texts[incorrect_index]
                    previous_equation = step_texts[previous_index]

                    corrected_equation = result.get(
                        "corrected_equation"
                    )

                    left_column, right_column = st.columns(
                        2,
                        gap="large"
                    )

                    with left_column:

                        with st.container(border=True):

                            st.markdown("#### Student's attempt")

                            st.error("Incorrect transformation")

                            st.code(
                                student_equation,
                                language="text"
                            )

                            st.caption(
                                f"Previous step: {previous_equation}"
                            )

                    with right_column:

                        with st.container(border=True):

                            st.markdown("#### Suggested correction")

                            if corrected_equation:

                                st.success("Corrected equation")

                                st.code(
                                    corrected_equation,
                                    language="text"
                                )

                            else:

                                st.info(
                                    "A corrected equation is not "
                                    "available for this error."
                                )

                    if corrected_equation:

                        st.markdown("**What changed?**")

                        st.info(
                            "Compare the student's attempt with "
                            "the suggested correction to understand "
                            "the mathematical change."
                        )

                else:

                    st.warning(
                        "The equations required for comparison "
                        "are not available."
                    )

            else:

                st.info(
                    "No specific incorrect transition is "
                    "available for comparison."
                )

            # ERROR INTELLIGENCE

            st.write("")

            st.markdown("### Error intelligence")

            with st.container(border=True):

                st.markdown("**Detected category**")

                category_names = {
                    "sign_error": "Sign error",
                    "possible_arithmetic_error": "Possible arithmetic error"
                }

                readable_category = category_names.get(
                    error_category,
                    str(error_category or "Unclassified error")
                )

                st.markdown(
                    f'<div class="status-pill">{readable_category}</div>',
                    unsafe_allow_html=True
                )

                explanation = result.get(
                    "explanation",
                    "The validator detected an inconsistent transition."
                )

                correction = result.get(
                    "correction",
                    "Review the mathematical operation used."
                )

                corrected_equation = result.get(
                    "corrected_equation"
                )

                st.markdown("#### What went wrong?")

                st.write(explanation)

                st.markdown("#### How to correct it")

                st.write(correction)

                if corrected_equation:

                    st.markdown("#### Suggested corrected equation")

                    st.code(
                        corrected_equation,
                        language="text"
                    )

        # REPORT FOOTNOTE

        st.divider()

        st.caption(
            "MathTrace AI is a research prototype using symbolic "
            "mathematics and rule-based validation. A passed result "
            "means the transitions were accepted by the current "
            "validation rules; it is not a guarantee that every "
            "possible mathematical issue has been detected."
        )


# ==================================================
# 12. FOOTER
# ==================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        ∑ MATH TRACE AI
        <br>
        MATHEMATICAL REASONING ENGINE
        <br>
        An AI-assisted symbolic mathematics research prototype.
    </div>
    """,
    unsafe_allow_html=True
)
