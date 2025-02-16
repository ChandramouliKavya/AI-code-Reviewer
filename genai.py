import streamlit as st
import google.generativeai as genai
from IPython.display import Markdown
import os


st.title(" :left_speech_bubble: An AI Code Reviewer")

# Load API key securely from a file
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

# Define system instructions
system_prompt = """You are a Python Developer tutor. You can resolve Python-related queries, 
review code, identify potential bugs, and suggest improvements. 
If someone asks about non-Python topics, politely request relevant queries only."""




# taking the prompt fom the user 
user_prompt = st.text_area("Enter your Python code :")

button = st.button(" :orange[Generate Review]")
# Extract and display response
if button == True:
    # Initialize Gemini model
    gemini = genai.GenerativeModel(model_name="gemini-1.5-pro", system_instruction=system_prompt)


    # Generate response
    response = gemini.generate_content(user_prompt)
    st.header("Code Review")
    st.header("Bug Report")
    st.markdown(response.text)

