import streamlit as st

st.set_page_config(
    page_title="Cypher.ai",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

# st.write("""
# [![view source code](https://img.shields.io/badge/GitHub%20-gray?logo=github)](https://github.com/jayeeed/langchain-chatbot)
# ![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fjayeeed%2Flangchain-chatbot&label=Visitors&countColor=%23263759&style=flat)
# """)

st.markdown("""
# :blue[Cypher.ai] 🤖
## Order your :rainbow[Personalized Chatbot] soon!
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/1_💬_QABot.py", label="Q/ABot", icon="💬")
    st.page_link("pages/2_⭐_ConvoBot.py", label="ConvoBot", icon="⭐")
    st.page_link("pages/5_🌐_NetBot.py", label="NetBot", icon="🌐")

with col2:
    st.page_link("pages/4_👨‍🌾_LangBot.py", label="LangBot", icon="👨‍🌾")
    st.page_link("pages/3_🇧🇩_BanglaBot.py", label="BanglaBot", icon="🇧🇩")
    st.page_link("pages/6_🔍_DocBot.py", label="DocBot", icon="🔍")
    
with col3:
    st.page_link("pages/7_👨‍💼_HRBot.py", label="HRBot", icon="👨‍💼")
    # st.page_link("pages/8_📖_SumBot.py", label="SumBot", icon="📖")

st.markdown("""
#### 1. What is :blue[Cypher.ai]? 

Cypher.ai offers a suite of **Chatbots** to help users interact with the data.

#### 2. What are the :blue[Chatbots] available?

- :green[**Q/ABot**]: Basic **Chatbot** that allows users to ask ***Questions*** and get ***Answers***.

- :green[**ConvoBot**]: Conversational **Chatbot** that allows users ***Chat*** and ***Remember*** their previous interactions.
         
- :green[**NetBot**]: Internet accessed **Chatbot** that allows users to ask questions about ***Latest*** events.
        
- :green[**DocBot**]: **Chatbot** that allows users to ask questions about ***Documents***.
         
- :green[**HRBot**]: **Chatbot** that allows users to ask questions about all ***Documents*** in the ***Directories***.
         
- :green[**SumBot**]: **Chatbot** that allows users to ask questions about ***Summerization*** of ***Documents***.

#### 3. How can I order :blue[Cypher.ai]?

- **[Email](mailto:jayedbinjahangir@gmail.com) &nbsp;&nbsp; [Portfolio](https://jayeeed.netlify.app/) &nbsp;&nbsp; [Linkedin](https://www.linkedin.com/in/xayed/)**

#### 4. How can I contact :blue[Cypher.ai]?

- **[Email](mailto:jayedbinjahangir@gmail.com) &nbsp;&nbsp; [Portfolio](https://jayeeed.netlify.app/) &nbsp;&nbsp; [Linkedin](https://www.linkedin.com/in/xayed/)**

#### 5. How can I get support for :blue[Cypher.ai]?

- **[Email](mailto:jayedbinjahangir@gmail.com) &nbsp;&nbsp; [Portfolio](https://jayeeed.netlify.app/) &nbsp;&nbsp; [Linkedin](https://www.linkedin.com/in/xayed/)**
         
""")

st.caption('Made with ❤️ by [Jayed](https://www.linkedin.com/in/xayed/)')