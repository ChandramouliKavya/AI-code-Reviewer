import streamlit as st
import google.generativeai as genai
import os

st.title("🚀 AI Code Reviewer")

# ✅ Load API Key Securely
api_key = os.getenv("GEMINI_API_KEY")

# ✅ Configure Gemini API
genai.configure(api_key=api_key)

# ✅ Initialize Model
gemini = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction="You are a Python tutor...")


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



