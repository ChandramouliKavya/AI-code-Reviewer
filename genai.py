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

gemini = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction="You are a Python tutor...")

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
    if user_prompt.strip():
        with st.spinner("Analyzing your code..."):
            response = gemini.generate_content(user_prompt, stream=True)  # Stream output
            
            st.subheader("🔍 Code Review")
            response_text = ""
            for chunk in response:
                response_text += chunk.text  # Append text chunks
                st.markdown(response_text)  # Show output as it comes



