import os
os.environ["USER_AGENT"] = "WebContextExplorer/2.0 (Bot for Personal Research)"

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

FAISS_STORAGE_PATH = "vector_db/faiss_index"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "llama-3.3-70b-versatile"

def get_api_key():
    """Retrieves API Key from .env or streamlit secrets safely."""
    key = os.getenv("GROQ_API_KEY")
    
    if not key:
        try:
            key = st.secrets.get("GROQ_API_KEY")
        except:
            key = None
    return key