import utils
import streamlit as st
from streaming import StreamHandler

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="ContextBot", page_icon="🇧🇩", initial_sidebar_state='collapsed')
st.page_link("Home.py", label="Back to Home", icon="🏠")

st.header('***Bengali*** Conversational Chatbot')
st.write('***Bengali*** Conversational **Chatbot** that allows users ***Chat*** and ***Remember*** their previous interactions.')

class BanglaBot:
    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo-0125"
        self.prompt_template = PromptTemplate.from_template(
            """
            You a helpful assistant that speaks {language}. Your name is {bot_name}.
            Answer as short as possible. Try to be as objective as possible.
            
            Answer in {language}: {user_query}
            """
        )

    @st.cache_resource
    def setup_chain(_self):
        memory = ConversationBufferMemory()
        llm = ChatOpenAI(model_name=_self.openai_model, temperature=0.1, streaming=True, max_tokens=1000)
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
                prompt = self.prompt_template.format(user_query=user_query, bot_name="BanglaCypher", language="Bengali")
                response = chain.run(user_query + " " + prompt, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    obj = BanglaBot()
    obj.main()
