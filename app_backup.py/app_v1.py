import streamlit as st
from chatbot import ask_ai

st.set_page_config(
    page_title="FitGenie AI",
    page_icon="🏋️",
    layout="wide"
)

st.title("🏋️ FitGenie AI")
st.subheader("Your AI Fitness Trainer")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask your fitness question...")

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):
        answer, sources = ask_ai(question)

    full_answer = answer + "\n\n### 📚 Sources\n"

    for source in sources:
        full_answer += f"- {source}\n"

    st.session_state.messages.append(
        {"role": "assistant", "content": full_answer}
    )

    with st.chat_message("assistant"):
        st.markdown(full_answer)