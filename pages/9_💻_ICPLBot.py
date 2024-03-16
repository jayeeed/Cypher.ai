import os
import utils
import streamlit as st
from streaming import StreamHandler

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import UnstructuredWordDocumentLoader

st.set_page_config(page_title="DocBot", page_icon="🔍", initial_sidebar_state='expanded')
st.page_link("Home.py", label="Back to Home", icon="🏠")

st.header('***Document*** Chatbot')
st.write('**Chatbot** that allows users to ask questions about ***Documents***.')


class DocBot:

    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo-0125"
        self.file_path= "./test/Profile_IPSITA_2024.docx"
        self.prompt_template = PromptTemplate.from_template(
            """
            You a helpful assistant that answer questions about IPSITA COMPUTERS PTE LTD. 
            Answer as short as possible. Try to be as objective as possible. Try to be as concise as possible. Answer in bullet points if relavant.
            
            Question: {user_query}
            Answer:
            """
        )

    @st.spinner('Analyzing documents..')
    def setup_qa_chain(self):

        loader = UnstructuredWordDocumentLoader(self.file_path)
        docs = loader.load()
        
        # Split documents
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
        )
        splits = text_splitter.split_documents(docs)

        # Create embeddings and store in vectordb
        embeddings = OpenAIEmbeddings()
        vectordb = Chroma.from_documents(splits, embeddings)

        # Define retriever
        retriever = vectordb.as_retriever(
            search_type='mmr',
            search_kwargs={'k':1, 'fetch_k':4}
        )

        # Setup memory for contextual conversation        
        memory = ConversationBufferMemory(
            memory_key='chat_history',
            return_messages=True
        )

        # Setup LLM and QA chain
        llm = ChatOpenAI(model_name=self.openai_model, temperature=0.1, streaming=True)
        qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory, verbose=True)
        return qa_chain


    @utils.enable_chat_history
    def main(self):
        user_query = st.chat_input(placeholder="Ask me anything!")

        if user_query:
            qa_chain = self.setup_qa_chain()

            utils.display_msg(user_query, 'user')

            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                prompt = self.prompt_template.format(user_query=user_query)
                response = qa_chain.run(prompt, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    obj = DocBot()
    obj.main()