import utils
import streamlit as st

from langchain.agents import AgentType, initialize_agent, Tool

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.callbacks import StreamlitCallbackHandler

from langchain_openai import ChatOpenAI

st.set_page_config(page_title="NetBot", page_icon="🌐")
st.header('Chatbot with Internet Access')
st.write('Internet accessed **Chatbot** that allows users to ask questions about ***Latest*** events.')

class NetBot:

    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo"

    def setup_agent(self):
        # Define tool
        ddg_search = DuckDuckGoSearchRun()
        tools = [
            Tool(
                name="DuckDuckGoSearch",
                func=ddg_search.run,
                description="Useful for when you need to answer questions about current events. You should ask targeted questions",
            )
        ]

        # Setup LLM and Agent
        llm = ChatOpenAI(model_name=self.openai_model, streaming=True)
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            handle_parsing_errors=True,
            verbose=True
        )
        return agent

    @utils.enable_chat_history
    def main(self):
        agent = self.setup_agent()
        user_query = st.chat_input(placeholder="Ask me anything!")
        if user_query:
            utils.display_msg(user_query, 'user')
            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(user_query, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.write(response)

if __name__ == "__main__":
    obj = NetBot()
    obj.main()