import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read the API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Streamlit App
st.title("🔍 AI Code Explainer")
st.write("Enter a code snippet below, and the AI will explain it in simple terms.")

# Code Input
code_input = st.text_area("Paste your code here:", height=300)

# Generate Explanation
if st.button("🤖 Explain Code") and code_input:
    try:
        # Use the Gemini model
        model = genai.GenerativeModel("gemini-1.5-pro-latest")

        # Generate Explanation
        response = model.generate_content(f"Explain the following code in simple terms:\n{code_input}")

        # Display Explanation
        if response and hasattr(response, 'text'):
            st.write("### 📜 Explanation:")
            st.write(response.text)
        else:
            st.error("Error: No explanation received.")
    except Exception as e:
        st.error(f"Error: {e}")
