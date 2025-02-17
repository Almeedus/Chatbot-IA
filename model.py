import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Diretório base e caminho do PDF
base_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(base_dir, "src", "edital_ifsp_itapetininga.pdf")

# Carregando documentos do PDF
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# Divisão dos textos
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Inicializando LangChain
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="ft:gpt-4o-2024-08-06:personal:fine-tuning2:AoGMkhl2"),
    retriever=vectorstore.as_retriever()
)
