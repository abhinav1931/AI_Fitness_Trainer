import os

from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

API_KEY = os.getenv("OLLAMA_API_KEY")

if not API_KEY:
    raise ValueError(
        "OLLAMA_API_KEY not found. Please add it to your .env file."
    )


# ============================================================
# LOCAL EMBEDDINGS
# ============================================================

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434"
)


# ============================================================
# LOAD CHROMA VECTOR DATABASE
# ============================================================

# vectorstore = Chroma(
#     persist_directory="vectorstore",
#     embedding_function=embeddings
# )

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
VECTORSTORE_DIR = BASE_DIR / "vectorstore"

vectorstore = Chroma(
    persist_directory=str(VECTORSTORE_DIR),
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)


# ============================================================
# OLLAMA CLOUD LLM
# ============================================================

llm = ChatOllama(
    model="gpt-oss:120b",
    temperature=0,
    base_url="https://ollama.com",
    client_kwargs={
        "headers": {
            "Authorization": f"Bearer {API_KEY}"
        }
    }
)


# ============================================================
# AI FUNCTION
# ============================================================

def ask_ai(question):

    # Retrieve relevant documents
    docs = retriever.invoke(question)

    # Combine retrieved text
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # Prompt
    prompt = f"""
You are FitGenie AI, a professional certified fitness trainer.

Use ONLY the provided context to answer the question.

Rules:

- Answer in clear and simple English.
- Use headings.
- Use bullet points.
- Never copy the PDF word-for-word.
- Explain exercises briefly.
- Keep the answer practical and easy to understand.
- Do not invent information.
- If the answer is not available in the context, reply exactly:

"I don't have enough information in my knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""

    # Get AI response
    response = llm.invoke(prompt)

    # Collect sources
    sources = []

    for doc in docs:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        if source not in sources:
            sources.append(source)

    return response.content, sources

if __name__ == "__main__":
    question = input("Ask FitGenie: ")

    answer, sources = ask_ai(question)

    print("\n===== FitGenie AI =====\n")
    print(answer)

    print("\n===== Sources =====")
    for source in sources:
        print("-", source)