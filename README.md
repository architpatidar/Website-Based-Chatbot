
# Website-Based-Chatbot



## 🚀 Project Overview


The Web Context Chatbot is a specialized AI tool designed to bridge the gap between static web content and interactive AI. By providing a URL, the system scrapes the live website, processes its text into manageable segments, and stores them in a local vector database. Users can then ask natural language questions and receive accurate answers derived exclusively from the indexed site, ensuring high relevance and reducing AI hallucinations.
## 🏗️ Architecture Explanation

The project follows a modular RAG (Retrieval-Augmented Generation) architecture, split into five core operations:

1.Ingestion & Processing: Uses WebBaseLoader to scrape URLs and RecursiveCharacterTextSplitter to break text into chunks with context-preserving overlap.

2.Vector Storage: Converts text chunks into high-dimensional vectors and stores them locally for rapid retrieval.

3.Standalone Query Rephrasing: Uses an LLM to rewrite user questions based on chat history, ensuring the search engine understands the full context of the conversation.

4.Retrieval: Searches the vector database for the most semantically relevant snippets to the user's query.

5.Generation: Passes the retrieved context and the query to the LLM to generate a final, grounded answer.
## 🛠️ Frameworks & Tools

● LangChain / LangGraph: Used as the primary orchestration framework to manage document loading, splitting, and the RAG chain logic.

● Streamlit: Provides the interactive web-based user interface for URL input and real-time chat.

● LLM Model: Llama 3.3-70b-versatile (via Groq): This model offers state-of-the-art performance in reasoning and text generation.

● Vector Database: FAISS (Local): FAISS (Facebook AI Similarity Search) is an industry-standard library for efficient similarity searching.

● Embedding Strategy
Model: sentence-transformers/all-MiniLM-L6-v2

## 💻 Setup and Run Instructions

 - Prerequisites

   - Python 3.9+
   - A Groq API Key (obtainable from Groq Cloud)

- Clone the project

```bash
git clone https://github.com/your-username/web-context-chatbot.git
cd web-context-chatbot
```
- Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

- Install Dependencies

```bash
pip install -r requirements.txt
```

- Environment Setup
```bash
Create a .env file in the root directory and add your key:
Plaintext
GROQ_API_KEY=your_api_key_here
```

- Run the Application

```bash
streamlit run app.py
```
## 📝 Assumptions, Limitations & Future Improvements

- Assumptions
  - User Connectivity: Assumes an active internet connection for web scraping and Groq API calls.

  - URL Accessibility: Assumes the provided URL is publicly accessible and not blocked by bot-detection or login screens.

- Limitations
  - Text Only: Currently processes text content; images, videos, and complex dynamic JavaScript-rendered content may be ignored.

  - Local Storage: The vector database is stored locally, meaning it must be re-indexed if the app is moved or the vector_db folder is cleared.

- Future Improvements
  - Support for PDFs: Allow users to upload local documents alongside URLs.

  - Dynamic Scraping: Integrate Playwright or Selenium to handle JavaScript-heavy websites.

  - Hybrid Search: Combine semantic search with keyword search (BM25) for better retrieval accuracy on specific terms.
