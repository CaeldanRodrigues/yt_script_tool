from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from utils import generate_script

st.title("YouTube Script Generator")
st.write("This is a simple web app to generate a script for a YouTube video by browsing the web.")

# Captures User Inputs
prompt = st.text_input('Topic of the video',key="prompt")  # The box for the text prompt
video_length = st.text_input('Expected Video Length 🕒 (in minutes)',key="video_length")  # The box for the text prompt
creativity = st.slider('Creativity - (0 LOW - 1 HIGH)', 0.0, 1.0, 0.2,step=0.1)

submit = st.button("Generate Script")

if submit:
        
    # call the generate_script function from utils
    search_result,title,script = generate_script(prompt,video_length,creativity)
    st.success('Here is your script ❤️')

    #Display Title
    st.subheader("Title:🔥")
    st.write(title)

    #Display Video Script
    st.subheader("Your Video Script:📝")
    st.write(script)

    #Display Search Engine Result
    st.subheader("Check Out - DuckDuckGo Search Results:🔍")
    with st.expander('Show me 👀'): 
            st.info(search_result)