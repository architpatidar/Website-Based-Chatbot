import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from utils import is_valid_url
from processor import scrape_and_chunk, save_to_vector_store, load_existing_db
from brain import initialize_brain
from config import get_api_key

st.set_page_config(page_title="Website Chatbot")
st.title("Website Chatbot")

with st.sidebar:
    st.header("Setup")
    site_url = st.text_input("Enter Website URL", placeholder="https://www.example.com")
    
    if st.button("Index Website"):
        if not is_valid_url(site_url):
            st.error("Please enter a valid URL (starting with http:// or https://).")
        elif not get_api_key():
            st.error("Missing GROQ_API_KEY in .env file.")
        else:
            with st.spinner("Analyzing website..."):
                chunks = scrape_and_chunk(site_url)
                if isinstance(chunks, str):
                    st.error(chunks)
                else:
                    save_to_vector_store(chunks)
                    st.success("Website indexed!")
                    st.session_state.chat_history = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    st.chat_message("human" if isinstance(msg, HumanMessage) else "ai").write(msg.content)

user_input = st.chat_input("What is this website about?")

if user_input:
    db = load_existing_db()
    if not db:
        st.warning("Please provide a URL and click 'Index Website' first.")
    else:
        st.chat_message("human").write(user_input)
        
        with st.chat_message("ai"):
            try:
                chain = initialize_brain(db)
                response = chain.invoke({"input": user_input, "chat_history": st.session_state.chat_history})
                answer = response["answer"]
                st.write(answer)
                
                st.session_state.chat_history.append(HumanMessage(content=user_input))
                st.session_state.chat_history.append(AIMessage(content=answer))
            except Exception as e:
                st.error(f"An error occurred: {e}")