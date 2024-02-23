import os
import utils
import streamlit as st
from streaming import StreamHandler

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch

from langchain_openai import ChatOpenAI

st.set_page_config(page_title="DirBot", page_icon="📁")
st.header('Chat with your documents')
st.write('Has access to custom documents and can respond to user queries by referring to the content within those documents')

class DirBot:

    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo"

    @st.spinner('Analyzing documents..')
    def setup_qa_chain(self, folder_path):
        # Load documents from the directory
        loader = DirectoryLoader(folder_path)
        docs = loader.load()

        # Split documents
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=200
        )
        splits = text_splitter.split_documents(docs)

        # Create embeddings and store in vectordb
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectordb = DocArrayInMemorySearch.from_documents(splits, embeddings)

        # Define retriever
        retriever = vectordb.as_retriever(
            search_type='mmr',
            search_kwargs={'k': 2, 'fetch_k': 4}
        )

        # Setup memory for contextual conversation
        memory = ConversationBufferMemory(
            memory_key='chat_history',
            return_messages=True
        )

        # Setup LLM and QA chain
        llm = ChatOpenAI(model_name=self.openai_model, temperature=0, streaming=True)
        qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory, verbose=True)
        return qa_chain

    @utils.enable_chat_history
    def main(self):

        # User Inputs
        folder_path = st.sidebar.text_input(label='Enter the folder path containing PDF files')
        if not os.path.exists(folder_path):
            st.error("Invalid folder path. Please provide a valid folder path.")
            st.stop()

        user_query = st.chat_input(placeholder="Ask me anything!")

        if folder_path and user_query:
            qa_chain = self.setup_qa_chain(folder_path)

            utils.display_msg(user_query, 'user')

            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                response = qa_chain.run(user_query, callbacks=[st_cb])
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    obj = DirBot()
    obj.main()
