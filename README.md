● Project Overview
The Web Context Chatbot is a specialized AI tool designed to bridge the gap between static web content and interactive AI. By providing a URL, the system scrapes the live website, processes its text into manageable segments, and stores them in a local vector database. Users can then ask natural language questions and receive accurate answers derived exclusively from the indexed site, ensuring high relevance and reducing AI hallucinations.

● Architecture Explanation
The project follows a modular RAG (Retrieval-Augmented Generation) architecture, split into five core operations:

Ingestion & Processing: Uses WebBaseLoader to scrape URLs and RecursiveCharacterTextSplitter to break text into chunks with context-preserving overlap.

Vector Storage: Converts text chunks into high-dimensional vectors and stores them locally for rapid retrieval.

Standalone Query Rephrasing: Uses an LLM to rewrite user questions based on chat history, ensuring the search engine understands the full context of the conversation.

Retrieval: Searches the vector database for the most semantically relevant snippets to the user's query.

Generation: Passes the retrieved context and the query to the LLM to generate a final, grounded answer.

● Frameworks Used
LangChain / LangGraph: Used as the primary orchestration framework to manage document loading, splitting, and the RAG chain logic.

Streamlit: Provides the interactive web-based user interface for URL input and real-time chat.

● LLM Model: Llama 3.3-70b-versatile (via Groq)
Why: This model offers state-of-the-art performance in reasoning and text generation.

Why Groq: Groq’s LPU (Language Processing Unit) architecture provides "lightning-fast" inference speeds, delivering nearly instantaneous responses compared to traditional GPU-based providers.

● Vector Database: FAISS (Local)
Why: FAISS (Facebook AI Similarity Search) is an industry-standard library for efficient similarity searching.

Local Advantage: It allows the vector store to be saved and reloaded locally (folder: vector_db/), eliminating the need for expensive cloud database hosting while maintaining high speed.

● Embedding Strategy
Model: sentence-transformers/all-MiniLM-L6-v2

Approach: This model maps sentences into a 384-dimensional dense vector space. It was chosen for its excellent balance of speed and semantic accuracy, specifically for short-to-medium length paragraphs typical of web content.

● Setup and Run Instructions
1. Prerequisites
Python 3.10+

A Groq API Key (obtainable from Groq Cloud)

2. Installation
Bash
# Clone the repository
git clone https://github.com/your-username/web-context-chatbot.git
cd web-context-chatbot

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
3. Environment Setup
Create a .env file in the root directory and add your key:

Plaintext
GROQ_API_KEY=your_api_key_here
4. Running the App
Bash
streamlit run app.py
● Assumptions, Limitations, and Improvements
Assumptions
User Connectivity: Assumes an active internet connection for web scraping and Groq API calls.

URL Accessibility: Assumes the provided URL is publicly accessible and not blocked by bot-detection or login screens.

Limitations
Text Only: Currently processes text content; images, videos, and complex dynamic JavaScript-rendered content may be ignored.

Local Storage: The vector database is stored locally, meaning it must be re-indexed if the app is moved or the vector_db folder is cleared.

Future Improvements
Support for PDFs: Allow users to upload local documents alongside URLs.

Dynamic Scraping: Integrate Playwright or Selenium to handle JavaScript-heavy websites.

Hybrid Search: Combine semantic search with keyword search (BM25) for better retrieval accuracy on specific terms.