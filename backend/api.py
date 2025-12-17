from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from rag_engine import RAGEngine
from contextlib import asynccontextmanager

engine: RAGEngine | None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global engine
    loop = asyncio.get_running_loop()
    # Initialize RAGEngine in thread to avoid blocking
    engine = await loop.run_in_executor(None, RAGEngine)
    yield

app = FastAPI(lifespan=lifespan)

class Query(BaseModel):
    question: str
    selected_text: str | None = None

@app.post("/chat")
async def chat(q: Query):
    if not engine:
        return {"error": "Chatbot not initialized"}

    loop = asyncio.get_running_loop()
    answer = await loop.run_in_executor(None, engine.answer, q.question, q.selected_text)
    return {"answer": answer}

@app.get("/health")
async def health():
    return {"status": "ok", "chatbot_available": engine is not None}
