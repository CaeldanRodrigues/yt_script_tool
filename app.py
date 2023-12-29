import streamlit as st

st.title("YouTube Script Generator")
st.write("This is a simple web app to generate a script for a YouTube video using OpenAI's GPT-3.5-Turbo.")

# Captures User Inputs
prompt = st.text_input('Topic of the video',key="prompt")  # The box for the text prompt
video_length = st.text_input('Expected Video Length 🕒 (in minutes)',key="video_length")  # The box for the text prompt
creativity = st.slider('Creativity - (0 LOW - 1 HIGH)', 0.0, 1.0, 0.2,step=0.1)

submit = st.button("Generate Script")