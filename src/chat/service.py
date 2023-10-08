from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

from src.chat.core.index import ChatIndex


class ChatService:
    def __init__(self):
        self.index = ChatIndex()
        self.llm = ChatOpenAI()

    def query(self, query):
        qa = RetrievalQA.from_chain_type(
            llm=self.llm, chain_type="stuff", retriever=self.index.index.as_retriever()
        )
        resp = qa.run(query)
        return resp
