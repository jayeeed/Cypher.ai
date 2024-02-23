import streamlit as st

st.set_page_config(
    page_title="Chatbot",
    page_icon='💬',
    layout='wide'
)

st.header("Chatbot Implementations with Langchain")
st.write("""
[![view source code](https://img.shields.io/badge/GitHub%20-gray?logo=github)](https://github.com/jayeeed/langchain-chatbot)
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fjayeeed%2Flangchain-chatbot&label=Visitors&countColor=%23263759&style=flat)
""")

st.write("""
Langchain is a powerful framework designed to streamline the development of applications using Language Models (LLMs). It provides a comprehensive integration of various components, simplifying the process of assembling them to create robust applications.

Leveraging the power of Langchain, the creation of chatbots becomes effortless. Here are a few examples of chatbot implementations catering to different use cases:

- **BasicBot**: Engage in interactive conversations with the LLM.
- **ContextBot**: A chatbot that remembers previous conversations and provides responses accordingly.
- **NetBot**: An internet-enabled chatbot capable of answering user queries about recent events.
- **DocBot**: Empower the chatbot with the ability to access custom documents, enabling it to provide answers to user queries based on the referenced information.
- **DirBot**: Empower the chatbot with the ability to access multiple documents, enabling it to provide answers to user queries based on the referenced information.
- **SumBot**: Empower the chatbot with the ability to access multiple documents, enabling it to provide summary to user queries based on the referenced information.

To explore sample usage of each chatbot, please navigate to the corresponding chatbot section.
""")