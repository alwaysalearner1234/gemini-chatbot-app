
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["AIzaSyCEJHfN7FC96Qijsni9aDXqt7Bvu9RKCa4"])

if "messages" not in st.session_state:
    st.session_state.messages = []

model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="Gemini AI Chatbot", page_icon="💬")
st.title("🤖 Gemini AI Chatbot")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = model.generate_content(
        [m["content"] for m in st.session_state.messages if m["role"] == "user"]
    )

    reply = response.text
    st.chat_message("ai").markdown(reply)
    st.session_state.messages.append({"role": "ai", "content": reply})
