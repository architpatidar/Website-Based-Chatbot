from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from config import get_api_key, LLM_MODEL

def initialize_brain(vectorstore):
    api_key = get_api_key()
    llm = ChatGroq(groq_api_key=api_key, model_name=LLM_MODEL, temperature=0.1)
    
    rephrase_template = ChatPromptTemplate.from_messages([
        ("system", "Consolidate the chat history and the new input into one standalone question."),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])

    qa_template = ChatPromptTemplate.from_messages([
        ("system", "Use the following context to answer the user's question. If the information isn't there, say exactly: 'The answer is not available on the provided website..'\n\nContext:\n{context}"),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])

    def execute_chain(inputs):
        history = inputs.get("chat_history", [])
        
        if history:
            rephrase_chain = rephrase_template | llm | StrOutputParser()
            query_to_search = rephrase_chain.invoke(inputs)
        else:
            query_to_search = inputs["input"]

        docs = vectorstore.as_retriever().invoke(query_to_search)
        context_text = "\n\n".join([doc.page_content for doc in docs])

        answer_chain = qa_template | llm | StrOutputParser()
        result = answer_chain.invoke({
            "context": context_text,
            "chat_history": history,
            "input": inputs["input"]
        })
        return {"answer": result}

    return RunnableLambda(execute_chain)