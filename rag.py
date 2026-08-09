from langchain_chroma import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings

# -----------------------------
# Load Embeddings
# -----------------------------
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# -----------------------------
# Load Vector Database
# -----------------------------
vectorstore = Chroma(
    persist_directory="vectorstore",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# -----------------------------
# Load LLM
# -----------------------------
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)

print("✅ RAG Ready!")
print("=" * 60)

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI Fitness Trainer.

Only answer from the context below.

If the answer is not available in the context,
say:
"I don't have enough information in my knowledge base."

Context:

{context}

Question:

{question}

Answer:
"""

    response = llm.invoke(prompt)

    print("\n🤖 AI Answer:\n")
    print(response.content)

    print("\n📚 Sources:")

    for doc in docs:
        print("-", doc.metadata["source"])