
import streamlit as st
from groq_client import gen_res
from local_ans import get_local_ans
from memory import store_mem

st.title("AI/ML Study Assistant")

if "memory" not in st.session_state:
    st.session_state.memory = store_mem()

if "chats" not in st.session_state:
    st.session_state.chats = []

for chat in st.session_state.chats:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

question = st.chat_input("Ask your question...")

if question:
    with st.chat_message("user"):
        st.write(question)

    memory = st.session_state.memory

    # 1. Check previous memory
    answer = memory.check_with_prev_ans(question)

    if answer is not None:
        source = "Memory"

    else:
        # 2. Check local answers
        answer = get_local_ans(question)

        if answer is not None:
            source = "Local"

        else:
            # 3. Call Groq API only if needed
            answer = gen_res(question, memory.get_hist())
            source = "Groq API"

    st.session_state.chats.append(
        {"role": "user", "content": question}
    )

    st.session_state.chats.append(
        {"role": "assistant", "content": answer}
    )

    memory.add_hist(question, answer)

    with st.chat_message("assistant"):
        st.caption(f"Source: {source}")
        st.write(answer)