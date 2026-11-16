
import streamlit as st
from sympy import Symbol
from mathtrace.validator import validate_text_solution_steps


# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="MathTrace AI",
    page_icon="∑",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =====================================================
# 2. DARK THEME
# =====================================================

st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap'
    );

    :root {
        --bg: #090E1B;
        --panel: #111A2B;
        --panel2: #151F34;
        --border: #293750;
        --text: #F1F4FC;
        --muted: #99A8C0;
        --accent: #8B9AFF;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 15% 0%,
                rgba(85, 104, 210, 0.13),
                transparent 35%
            ),
            #090E1B;
        color: var(--text);
        font-family: 'Inter', sans-serif;
    }

    .block-container {
        max-width: 1180px;
        padding: 2rem 2rem 3rem 2rem;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3, h4, p, label {
        color: var(--text);
    }

    /* Header */

    .brand-symbol {
        font-size: 34px;
        font-weight: 800;
        color: #AAB6FF;
    }

    .brand-name {
        font-size: 23px;
        font-weight: 800;
        color: #F1F4FC;
        letter-spacing: -0.7px;
    }

    .brand-caption {
        font-size: 11px;
        letter-spacing: 1.8px;
        color: #8C9AB4;
    }

    /* Hero */

    .eyebrow {
        color: #A6B2FF;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 2px;
    }

    .hero-title {
        color: #F1F4FC;
        font-size: 43px;
        font-weight: 800;
        letter-spacing: -1.8px;
        line-height: 1.2;
    }

    .hero-description {
        color: #9AA8C0;
        font-size: 15px;
        line-height: 1.8;
        max-width: 690px;
    }

    /* Panels */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(17, 26, 43, 0.92);
        border: 1px solid #293750;
        border-radius: 16px;
        padding: 20px;
    }

    .panel-label {
        color: #A6B2D0;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.6px;
    }

    .panel-title {
        color: #F1F4FC;
        font-size: 19px;
        font-weight: 700;
    }

    .panel-description {
        color: #99A8C0;
        font-size: 13px;
        line-height: 1.7;
    }

    /* Input */

    .stTextArea textarea {
        background: #0B1425 !important;
        color: #E9EEFF !important;
        border: 1px solid #34425E !important;
        border-radius: 10px !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 14px !important;
        line-height: 1.9 !important;
    }

    .stTextArea textarea:focus {
        border-color: #8798FF !important;
        box-shadow: 0 0 0 1px #8798FF !important;
    }

    /* Button */

    .stButton > button {
        width: 100%;
        min-height: 47px;
        border-radius: 10px;
        background: linear-gradient(110deg, #6579E8, #8370E8);
        color: white;
        border: 1px solid #8B9AFF;
        font-weight: 700;
    }

    .stButton > button:hover {
        background: linear-gradient(110deg, #788AFF, #9580F4);
        color: white;
        border-color: #AAB6FF;
    }

    /* Guide steps */

    .step-number {
        color: #AAB6FF;
        font-size: 13px;
        font-weight: 700;
    }

    .step-title {
        color: #EDF1FF;
        font-size: 14px;
        font-weight: 700;
    }

    .step-description {
        color: #9AA8C0;
        font-size: 12px;
        line-height: 1.7;
    }

    /* Example */

    .example {
        background: #0B1425;
        border: 1px solid #293750;
        border-radius: 10px;
        padding: 13px;
        color: #B8C5FF;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 12px;
        line-height: 2;
    }

    /* Footer */

    .footer {
        text-align: center;
        color: #8291AA;
        font-size: 12px;
        line-height: 1.8;
    }

    hr {
        border-color: #293750 !important;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 1rem;
        }

        .hero-title {
            font-size: 32px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =====================================================
# 3. HEADER
# =====================================================

header_left, header_right = st.columns([4, 1])

with header_left:
    logo_column, name_column = st.columns([0.55, 5])

    with logo_column:
        st.markdown(
            '<div class="brand-symbol">∑</div>',
            unsafe_allow_html=True
        )

    with name_column:
        st.markdown(
            '<div class="brand-name">MathTrace AI</div>'
            '<div class="brand-caption">'
            'ALGEBRA · REASONING · FEEDBACK'
            '</div>',
            unsafe_allow_html=True
        )

with header_right:
    st.markdown("🟢 **Prototype**")

st.divider()


# =====================================================
# 4. HERO SECTION
# =====================================================

st.markdown(
    '<div class="eyebrow">'
    'INTELLIGENT MATHEMATICS LEARNING'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-title">
        Understand every step.<br>
        Not just the final answer.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-description">
        Trace your algebraic reasoning, identify the first
        incorrect transformation, and understand how to
        correct your mathematical work.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")


# =====================================================
# 5. MAIN WORKSPACE
# =====================================================

input_column, guide_column = st.columns(
    [1.55, 0.85],
    gap="large"
)


# -----------------------------------------------------
# INPUT PANEL
# -----------------------------------------------------

with input_column:

    with st.container(border=True):

        st.markdown(
            '<div class="panel-label">'
            'YOUR MATHEMATICAL WORKSPACE'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="panel-title">Check your solution</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="panel-description">'
            'Enter each equation on a separate line. '
            'Show your working step by step.'
            '</div>',
            unsafe_allow_html=True
        )

        solution_text = st.text_area(
            "Solution steps",
            placeholder=(
                "2*x + 3 = 11\n"
                "2*x = 8\n"
                "x = 4"
            ),
            height=230,
            label_visibility="collapsed"
        )

        st.caption(
            "Use variable x and explicit multiplication (*), "
            "for example: 2*x."
        )

        check_button = st.button(
            "Analyze my solution →",
            type="primary"
        )


# -----------------------------------------------------
# GUIDE PANEL
# -----------------------------------------------------

with guide_column:

    with st.container(border=True):

        st.markdown(
            '<div class="panel-title">'
            'How MathTrace works'
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            '<div class="step-number">01</div>'
            '<div class="step-title">Enter your steps</div>'
            '<div class="step-description">'
            'Write each equation in the order you solved it.'
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            '<div class="step-number">02</div>'
            '<div class="step-title">Verify transformations</div>'
            '<div class="step-description">'
            'Compare consecutive equations using symbolic mathematics.'
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            '<div class="step-number">03</div>'
            '<div class="step-title">Understand the error</div>'
            '<div class="step-description">'
            'Review supported error patterns and suggested corrections.'
            '</div>',
            unsafe_allow_html=True
        )

        st.divider()

        st.markdown(
            '<div class="panel-label">EXAMPLE INPUT</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="example">
                2*x + 3 = 11<br>
                2*x = 8<br>
                x = 4
            </div>
            """,
            unsafe_allow_html=True
        )


# =====================================================
# 6. VALIDATION
# =====================================================

if check_button:

    step_texts = [
        line.strip()
        for line in solution_text.splitlines()
        if line.strip()
    ]

    st.divider()

    st.markdown(
        '<div class="panel-title">Analysis results</div>',
        unsafe_allow_html=True
    )

    if len(step_texts) < 2:

        st.warning(
            "Please enter at least two mathematical steps."
        )

    else:

        result = validate_text_solution_steps(
            step_texts,
            Symbol("x")
        )

        if result["status"] == "valid":

            st.success(
                "All solution steps passed validation."
            )

            with st.container(border=True):
                st.subheader("✓ Solution verified")
                st.write(
                    "Every consecutive equation pair passed "
                    "the current solution-set comparison."
                )

        elif result["status"] == "invalid":

            error_step = result["error_step"]

            st.error(
                f"Incorrect transformation detected at "
                f"step {error_step}."
            )

            category_names = {
                "sign_error": "Sign error",
                "possible_arithmetic_error":
                    "Possible arithmetic error"
            }

            error_category = result.get("error_category")

            st.markdown(
                "**Detected pattern:** "
                + category_names.get(
                    error_category,
                    "Unclassified transformation error"
                )
            )

            previous_column, next_column = st.columns(2)

            with previous_column:
                st.caption("PREVIOUS EQUATION")
                st.code(
                    step_texts[error_step - 1],
                    language="text"
                )

            with next_column:
                st.caption("YOUR NEXT EQUATION")
                st.code(
                    step_texts[error_step],
                    language="text"
                )

            st.markdown("**Why this step needs attention**")

            st.info(
                result.get(
                    "explanation",
                    "The transformation could not be validated."
                )
            )

            if result.get("correction"):
                st.markdown("**How to correct it**")
                st.write(result["correction"])

            if result.get("corrected_equation"):
                st.markdown("**Suggested corrected equation**")
                st.code(
                    result["corrected_equation"],
                    language="text"
                )

        elif result["status"] == "invalid_input":

            st.warning(
                "We couldn't understand the mathematical input."
            )

            st.write(result.get("message"))

        else:

            st.warning(
                result.get(
                    "message",
                    "Unable to validate this solution."
                )
            )


# =====================================================
# 7. FOOTER
# =====================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        <b>∑ MathTrace AI</b><br>
        An explainable algebra step-checking research prototype.<br>
        Built with Python · SymPy · Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
