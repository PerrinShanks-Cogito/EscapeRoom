import streamlit as st

st.set_page_config(page_title="Escape Room Challenge", page_icon="🔐")

st.title("🔐 Escape Room Challenge")
st.subheader("Mission 2: Identify the SMART Aim")

st.write("""
Review each draft aim statement and score it against the SMART criteria.

When you have identified the best SMART aim, select it below.
""")

options = {
    "A": "Reduce falls on Ward 8.",
    "B": "Reduce inpatient falls on Ward 8 by 30% within 6 months, as measured by monthly incident reports.",
    "C": "Improve the overall safety culture of Ward 8.",
    "D": "Eliminate all patient falls on Ward 8, permanently, starting tomorrow.",
    "E": "Increase the number of falls risk assessments completed on admission."
}

for key, value in options.items():
    st.markdown(f"**{key}**. {value}")

choice = st.radio(
    "Which statement is the best SMART Aim?",
    options.keys(),
    format_func=lambda x: f"{x}: {options[x]}"
)

if st.button("Check Answer"):

    if choice == "B":

        st.success("✅ Correct!")

        st.markdown("""
### Why B is correct

✔ Specific  
✔ Measurable  
✔ Achievable  
✔ Relevant  
✔ Time-bound
""")

        st.info("""
To unlock the code:

Find the two numbers in the aim statement.

**30** and **6**
""")

        st.code("306")

        st.balloons()

    else:

        reasons = {
            "A": "No target and no timeframe.",
            "C": "Not measurable and not specific to falls.",
            "D": "Not realistic or achievable.",
            "E": "This is a process measure rather than an outcome aim."
        }

        st.error("❌ Not quite")
        st.write(reasons[choice])

st.divider()

with st.expander("Need a Hint?"):
    st.write("""
The best SMART aim should tell you:

- What will improve
- By how much
- By when
- How success will be measured
""")
