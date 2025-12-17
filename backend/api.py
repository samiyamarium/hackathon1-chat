from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from contextlib import asynccontextmanager
from rag_engine import RAGEngine

engine: RAGEngine | None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global engine
    loop = asyncio.get_running_loop()
    engine = await loop.run_in_executor(None, RAGEngine)
    yield

app = FastAPI(lifespan=lifespan)

class Query(BaseModel):
    question: str
    selected_text: str | None = None

@app.post("/chat")
async def chat(q: Query):
    loop = asyncio.get_running_loop()
    answer = await loop.run_in_executor(None, engine.answer, q.question, q.selected_text)
    return {"answer": answer}

@app.get("/health")
async def health():
    return {"status": "ok", "chatbot_available": engine is not None}
