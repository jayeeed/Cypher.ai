import os
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

def enable_chat_history(func):
    if os.environ.get("OPENAI_API_KEY"):

        # to clear chat history after swtching chatbot
        current_page = func.__qualname__
        if "current_page" not in st.session_state:
            st.session_state["current_page"] = current_page
        if st.session_state["current_page"] != current_page:
            try:
                st.cache_resource.clear()
                del st.session_state["current_page"]
                del st.session_state["messages"]
            except:
                pass

        # to show chat history on ui
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
        for msg in st.session_state["messages"]:
            st.chat_message(msg["role"]).write(msg["content"])

    def execute(*args, **kwargs):
        func(*args, **kwargs)
    return execute

def display_msg(msg, author):
    st.session_state.messages.append({"role": author, "content": msg})
    st.chat_message(author).write(msg)

def configure_openai_api_key():
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        st.error("Please add your Valid/Working OpenAI API key to the .env file.")
        st.info("Obtain your key from this link: https://platform.openai.com/account/api-keys")
        st.stop()

    os.environ['OPENAI_API_KEY'] = openai_api_key
    return openai_api_key

configure_openai_api_key()