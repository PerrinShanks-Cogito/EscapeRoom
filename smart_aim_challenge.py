import streamlit as st

st.set_page_config(
    page_title="Challenge 2: SMART Aim",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Challenge 2: The SMART Aim Puzzle")

st.markdown("""
Nurse Patel has found five draft aim statements.

Only one is a true SMART aim.

Score each statement from **0 to 5** based on how many SMART criteria it meets.
""")

options = {
    "A": "Reduce falls on Ward 8.",
    "B": "Reduce inpatient falls on Ward 8 by 30% within 6 months, as measured by monthly incident reports.",
    "C": "Improve the overall safety culture of Ward 8.",
    "D": "Eliminate all patient falls on Ward 8, permanently, starting tomorrow.",
    "E": "Increase the number of falls risk assessments completed on admission."
}

expected = {
    "A": 2,
    "B": 5,
    "C": 1,
    "D": 2,
    "E": 3
}

answers = {}

st.divider()

for key, statement in options.items():

    col1, col2 = st.columns([4, 1])

    with col1:
        st.write(f"**{key}.** {statement}")

    with col2:
        answers[key] = st.selectbox(
            "Score",
            [0, 1, 2, 3, 4, 5],
            key=f"score_{key}",
            label_visibility="collapsed"
        )

st.divider()

if st.button("Submit Answers", type="primary"):

    correct = True

    for option, score in answers.items():
            if score != expected[option]:
            e

    if correct:

        st.success("✅ Excellent. You have identified the SMART aim.")

        st.markdown("""
### Why Option B is Correct

✅ **Specific**  
✅ **Measurable**  
✅ **Achievable**  
✅ **Relevant**  
✅ **Time-bound**

The clue is hidden in the statement.
""")

        st.info("""
Extract the two numbers from the SMART aim:

**30** and **6**
""")

        st.code("ESCAPE CODE: 306")

        st.balloons()

    else:

        st.error("❌ Not quite. Review the statements and try again.")

        feedback = {
            "A": "No target and no timeframe.",
            "C": "Not measurable and not specific to falls.",
            "D": "Not realistic or achievable.",
            "E": "A process measure rather than an outcome aim."
        }

        st.markdown("### Hints")

        for option in ["A", "C", "D", "E"]:
            st.write(f"**{option}:** {feedback[option]}")

with st.expander("Need a Hint?"):
    st.write("""
Ask yourself:

• Does the aim specify exactly what will improve?  
• Is there a numerical target?  
• Is it realistic?  
• Does it relate to the problem?  
• Is there a clear timeframe?
""")
