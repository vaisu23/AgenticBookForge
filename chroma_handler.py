import chromadb
import uuid
from sentence_transformers import SentenceTransformer

chroma_client = chromadb.PersistentClient(path="chroma_store")

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Embedding function using MiniLM
def get_embedding(text: str) -> list:
    embedding = embedding_model.encode(text)
    return embedding.tolist()

# Store version in ChromaDB
def store_version(text: str, metadata: dict):
    # embedding = get_embedding(text)
    # print("🔍 Generated embedding for the text.", embedding)

    collection = chroma_client.get_or_create_collection(name="book_versions")

    collection.add(
        documents=[text],
        metadatas=[metadata],
        ids=[str(uuid.uuid4())],
        # embeddings=[embedding]
    )
    # results = collection.get()
    # embeddings = results["embeddings"]

    # documents = results["documents"]
    # metadatas = results["metadatas"]
    # print("embedings", embeddings)
    # print("documents", documents)       
    # print("embeddings", embeddings)


    print(" Stored and persisted to ChromaDB.")
