import utils
import streamlit as st
from streaming import StreamHandler

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="CodeBot", page_icon="💻", initial_sidebar_state='expanded')
st.page_link("Home.py", label="Back to Home", icon="🏠")

st.header('***Code*** Conversational Chatbot')
st.write('Conversational **Chatbot** that allows users ***Develop*** and ***Test*** their code.')


class CodeBot:
    
    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo-0125"
        self.languages = ["", "Python", "Javascript", "Typescript", "Rust", "Java", "C++", "C#"]
        self.complexity = ["Simple", "Moderate", "Complex"]
        self.comment = ["With", "Without"]

        self.selected_language = st.sidebar.selectbox("Select Language:", options=self.languages)
        self.selected_complexity = st.sidebar.selectbox("Select Complexity:", options=self.complexity)
        self.selected_comment = st.sidebar.selectbox("Add Comments:", options=self.comment)

        self.prompt_template = PromptTemplate.from_template(
            """
            You a helpful assistant that generate {complexity} code in {language} {comment} comments.
            
            Answer in {language}: {user_query}
            """
        )


    @st.cache_resource
    def setup_chain(_self):
        memory = ConversationBufferMemory()
        llm = ChatOpenAI(model_name=_self.openai_model, temperature=0.1, streaming=True, max_tokens=4098)
        chain = ConversationChain(llm=llm, memory=memory, verbose=True)
        return chain
    

    @utils.enable_chat_history
    def main(self):
        chain = self.setup_chain()
        user_query = st.chat_input(placeholder="Ask me anything!")
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                
                prompt = self.prompt_template.format(
                    user_query=user_query, 
                    language=self.selected_language, 
                    complexity=self.selected_complexity, 
                    comment=self.selected_comment)
                
                response = chain.run(user_query + " " + prompt, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    obj = CodeBot()
    obj.main()
