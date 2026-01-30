from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from config import FAISS_STORAGE_PATH, EMBEDDING_MODEL
import os

def scrape_and_chunk(url):
    try:
        loader = WebBaseLoader(url)
        raw_data = loader.load()
        
        if not raw_data:
            return "Unable to extract content from this URL."

        splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
        chunks = splitter.split_documents(raw_data)
        return chunks
    except Exception as e:
        return f"Scraping error: {str(e)}"

def save_to_vector_store(chunks):
    embed_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    db = FAISS.from_documents(chunks, embed_model)
    
    if not os.path.exists("vector_db"):
        os.makedirs("vector_db")
        
    db.save_local(FAISS_STORAGE_PATH)
    return db

def load_existing_db():
    if os.path.exists(FAISS_STORAGE_PATH):
        embed_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        return FAISS.load_local(FAISS_STORAGE_PATH, embed_model, allow_dangerous_deserialization=True)
    return None