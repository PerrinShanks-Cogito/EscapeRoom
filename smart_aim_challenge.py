import streamlit as st

st.title("Escape Room Challenge")

st.components.v1.iframe(
    "https://your-h5p-url",
    height=800,
    scrolling=True
)
