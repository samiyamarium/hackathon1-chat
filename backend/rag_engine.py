import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

load_dotenv()

class RAGEngine:
    def __init__(self):
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        QDRANT_URL = os.getenv("QDRANT_URL")
        QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
        self.collection = os.getenv("QDRANT_COLLECTION")
        self.embed_model = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

        if not all([GEMINI_API_KEY, QDRANT_URL, QDRANT_API_KEY, self.collection]):
            raise RuntimeError("Missing environment variables!")

        # Embeddings
        self.embedder = SentenceTransformer(self.embed_model)

        # LLM
        genai.configure(api_key=GEMINI_API_KEY)
        self.llm = genai.GenerativeModel("gemini-2.0-flash")

        # Qdrant
        self.qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

        # Ensure collection exists
        existing = [c.name for c in self.qdrant.get_collections().collections]
        if self.collection not in existing:
            self.qdrant.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(
                    size=self.embedder.get_sentence_embedding_dimension(),
                    distance=Distance.COSINE
                )
            )

    def embed_text(self, text: str) -> list[float]:
        return self.embedder.encode(text).tolist()

    def search(self, query: str, top_k: int = 5) -> list[str]:
        query_vector = self.embed_text(query)
        hits = self.qdrant.search(
            collection_name=self.collection,
            query_vector=query_vector,
            limit=top_k
        )
        return [h.payload.get("text", "") for h in hits]

    def answer(self, question: str, selected_text: str | None = None) -> str:
        context = selected_text or "\n\n".join(self.search(question))
        prompt = f"""
You are a RAG assistant for a robotics book.
Answer ONLY from the following context.

### CONTEXT
{context}

### QUESTION
{question}

### ANSWER:
"""
        response = self.llm.generate_content(prompt)
        return response.text
