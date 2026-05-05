import streamlit as st
from dsa_chatbot import DSAChatbot

st.set_page_config(page_title="DSA Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 DSA Chatbot")
st.caption("Ask me anything about Data Structures and Algorithms")

# Initialize chatbot
if "chatbot" not in st.session_state:
    try:
        st.session_state.chatbot = DSAChatbot()
    except Exception as e:
        st.error(f"Failed to initialize chatbot: {e}")
        st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask a DSA question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chatbot.get_response(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})