import utils
import streamlit as st
from streaming import StreamHandler

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

st.set_page_config(page_title="BasicBot", page_icon="💬", initial_sidebar_state='collapsed')
st.page_link("Home.py", label="Back to Home", icon="🏠")

st.header('***Basic*** Chatbot')
st.write('Basic **Chatbot** that allows users to ask ***Questions*** and get ***Answers***.')

class QABot:
    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo-0125"
    
    def setup_chain(self):
        llm = ChatOpenAI(model_name=self.openai_model, temperature=0.1, streaming=True, max_tokens=1000)
        chain = ConversationChain(llm=llm, verbose=True)
        return chain
    
    @utils.enable_chat_history
    def main(self):
        chain = self.setup_chain()
        user_query = st.chat_input(placeholder="Ask me anything!")
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                response = chain.invoke(user_query, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    obj = QABot()
    obj.main()