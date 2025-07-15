
# Gemini Chatbot App

A simple AI chatbot powered by **Google Gemini Pro** and built with **Streamlit**.

## Features
- Chat with Gemini AI
- Memory using Streamlit session state
- API key secured with `.streamlit/secrets.toml`

## Setup Instructions

1. Extract the zip file.
2. Open `.streamlit/secrets.toml` and add your API key:
   ```toml
   GEMINI_API_KEY = "your-api-key-here"
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```
