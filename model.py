import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

base_dir = os.path.dirname(os.path.abspath(__file__))

def load_qa_chain_for_section(section_name: str):
    filename_map = {
        "Emails de contato": "datas_importantes.pdf",
        "Emails de contato": "emails_de_contato.pdf",
        "Locais de Prova": "locais_de_prova.pdf",
    }

    pdf_filename = filename_map.get(section_name.lower(), "edital_ifsp_itapetininga.pdf")
    pdf_path = os.path.join(base_dir, "src", pdf_filename)

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="ft:gpt-4o-2024-08-06:personal:fine-tuning:B1zlL1M4"),
        retriever=vectorstore.as_retriever()
    )
    return qa_chain
