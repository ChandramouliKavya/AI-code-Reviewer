import streamlit as st
import google.generativeai as genai
import os
import time

# 🎯 App Title
st.title("🚀 AI Code Reviewer")

# ✅ Load API Key Securely
api_key = os.getenv("GEMINI_API_KEY")

# ✅ Configure Gemini API
genai.configure(api_key=api_key)

# ✅ Initialize Model (Faster Model)
gemini = genai.GenerativeModel(model_name="gemini-1.5-pro", system_instruction="You are a Python tutor...")

# ✅ Cache API Calls to Reduce Response Time
@st.cache_data
def get_review(prompt):
    start_time = time.time()  # Measure API response time
    response = gemini.generate_content(prompt).text
    end_time = time.time()
    return response, round(end_time - start_time, 2)  # Return response + time taken

# 🎯 User Input
user_prompt = st.text_area("Enter your Python code:")

# 🎯 Button to Generate Review
if st.button("🔍 Generate Review"):
    if not user_prompt.strip():
        st.warning("Please enter some Python code before generating a review.")
    else:
        with st.spinner("Analyzing your code..."):
            response_text, response_time = get_review(user_prompt)  # Cached API Call

        # ✅ Display Results
        st.subheader("🔍 Code Review")
        st.markdown(response_text)
        st.success(f"✅ Review generated in {response_time} seconds")


