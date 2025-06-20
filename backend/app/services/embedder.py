import os
import pinecone
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENV"))
index = pinecone.Index(os.getenv("PINECONE_INDEX_NAME"))

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks, doc_id):
    vectors = []
    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk).tolist()
        metadata = {"doc_id": doc_id, "chunk_id": i, "text": chunk}
        vectors.append((f"{doc_id}_{i}", embedding, metadata))
    index.upsert(vectors=vectors)
    return len(vectors)

def get_relevant_chunks(question, doc_id, top_k=3):
    query_embedding = model.encode(question).tolist()
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True,
        filter={"doc_id": {"$eq": doc_id}}
    )
    return results["matches"]