from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Configurações iniciais
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("A chave OPENAI_API_KEY não foi encontrada. Verifique o arquivo .env.")

# Inicializar FastAPI
app = FastAPI()

# Modelo de entrada
class QueryRequest(BaseModel):
    query: str

# Inicializar LangChain (Pré-carregamento do PDF e configuração)
pdf_path = "C:\\Users\\eduar\\OneDrive\\Documentos\\Langchain\\src\\edital_ifsp_itapetininga.pdf"  # Substitua pelo caminho do PDF
loader = PyPDFLoader(pdf_path)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4"),
    retriever=vectorstore.as_retriever()
)

# Endpoint para responder perguntas
@app.post("/duvidas")
async def answer_query(request: QueryRequest):
    try:
        response = qa_chain.run(request.query)
        return {"query": request.query, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint de teste
@app.get("/")
async def root():
    return {"message": "API Funcionando!"}
