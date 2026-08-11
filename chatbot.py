import os
import streamlit as st

from langchain_chroma import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings


# --------------------------------
# Ollama Cloud API Key
# --------------------------------

OLLAMA_API_KEY = st.secrets["OLLAMA_API_KEY"]

os.environ["OLLAMA_API_KEY"] = OLLAMA_API_KEY


# --------------------------------
# Ollama Cloud Authentication
# --------------------------------

client_kwargs = {
    "headers": {
        "Authorization": f"Bearer {OLLAMA_API_KEY}"
    }
}


# --------------------------------
# Load Embeddings
# --------------------------------

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="https://ollama.com",
    client_kwargs=client_kwargs
)


# --------------------------------
# Load Vector Database
# --------------------------------

vectorstore = Chroma(
    persist_directory="vectorstore",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


# --------------------------------
# Load LLM
# --------------------------------

llm = ChatOllama(
    model="gpt-oss:20b",
    temperature=0,
    base_url="https://ollama.com",
    client_kwargs=client_kwargs
)


# --------------------------------
# AI Function
# --------------------------------

def ask_ai(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are FitGenie AI, a professional certified fitness trainer.

Use ONLY the provided context.

Rules:

- Answer in clear and simple English.
- Use headings.
- Use bullet points.
- Never copy the PDF word-for-word.
- Explain exercises briefly.
- If the answer is not available in the context, reply:
  "I don't have enough information in my knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    sources = []

    for doc in docs:
        source = doc.metadata.get("source", "Unknown")

        if source not in sources:
            sources.append(source)

    return response.content, sources