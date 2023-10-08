from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma


class ChatIndex:
    def __init__(self, rebuild_source_file=None):
        self.persist_directory = "./src/chat/chroma_db"
        self.embeddings = OpenAIEmbeddings()

        if rebuild_source_file is not None:
            self.index = self.build_index(rebuild_source_file)
        else:
            self.index = self.load_index()

    def load_index(self):
        db = Chroma(
            persist_directory=self.persist_directory, embedding_function=self.embeddings
        )
        return db

    def build_index(self, rebuild_source_file):
        loader = TextLoader(rebuild_source_file)
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(loader.load())

        db = Chroma.from_documents(
            docs, self.embeddings, persist_directory=self.persist_directory
        )
        db.persist()

        return db
