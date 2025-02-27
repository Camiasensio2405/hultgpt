import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🤖 HultGPT - Your AI Chatbot")
st.write("Ask me anything!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.text_input("Type your message here:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # **✅ Correct OpenAI API usage**
    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."}] + st.session_state.messages
    )

    bot_message = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": bot_message})

    with st.chat_message("assistant"):
        st.markdown(bot_message)

