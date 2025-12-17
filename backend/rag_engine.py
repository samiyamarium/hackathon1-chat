import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# Load env
load_dotenv()

class RAGEngine:
    def __init__(self):
        # ---- Environment Variables ----
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        QDRANT_URL = os.getenv("QDRANT_URL")
        QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
        self.collection = os.getenv("QDRANT_COLLECTION")
        self.embed_model = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

        if not all([GEMINI_API_KEY, QDRANT_URL, QDRANT_API_KEY, self.collection]):
            raise RuntimeError("❌ Missing environment variables")

        # ---- Embedding Model ----
        self.embedder = SentenceTransformer(self.embed_model)

        # ---- Gemini LLM ----
        genai.configure(api_key=GEMINI_API_KEY)
        self.llm = genai.GenerativeModel("gemini-2.0-flash")

        # ---- Qdrant Client ----
        self.qdrant = QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY
        )

        # ---- Ensure collection exists ----
        existing = [c.name for c in self.qdrant.get_collections().collections]
        if self.collection not in existing:
            self.qdrant.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(
                    size=self.embedder.get_sentence_embedding_dimension(),
                    distance=Distance.COSINE
                )
            )

    # ---------------- EMBEDDING ----------------
    def embed_text(self, text: str) -> list[float]:
        return self.embedder.encode(text).tolist()

    # ---------------- SEARCH ----------------
    def search(self, query: str, top_k: int = 5) -> list[str]:
        query_vector = self.embed_text(query)
        try:
            results = self.qdrant.search_points(
                collection_name=self.collection,
                query_vector=query_vector,
                limit=top_k
            )
            # results.result contains list of points
            return [p.payload.get("text", "") for p in results.result]
        except Exception as e:
            print(f"[Qdrant Search Error] {e}")
            return []

    # ---------------- ANSWER ----------------
    def answer(self, question: str, selected_text: str | None = None) -> str:
        try:
            context = selected_text or "\n\n".join(self.search(question, top_k=5))
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
        except Exception as e:
            print(f"[LLM Error] {e}")
            return f"[Error generating answer: {e}]"
