import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

print("=" * 60)
print("🏋️ AI Fitness Trainer - Creating Knowledge Base")
print("=" * 60)

# -----------------------------
# Paths
# -----------------------------
DATA_PATH = "data"
DB_PATH = "vectorstore"

# -----------------------------
# Load PDFs
# -----------------------------
loader = DirectoryLoader(
    DATA_PATH,
    glob="**/*.pdf",
    loader_cls=PyPDFLoader,
)

documents = loader.load()

print(f"✅ Loaded {len(documents)} pages.")

# -----------------------------
# Split Text
# -----------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

chunks = splitter.split_documents(documents)

print(f"✅ Created {len(chunks)} chunks.")

# -----------------------------
# Embeddings
# -----------------------------
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# -----------------------------
# Create Chroma DB
# -----------------------------
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH,
)

print("\n🎉 Vector Database Created Successfully!")
print("=" * 60)