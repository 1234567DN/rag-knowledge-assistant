from fastapi import FastAPI, Query
from .rag import Retriever, load_markdown_folder

app = FastAPI(title="RAG Knowledge Assistant", version="1.0.0")
retriever = Retriever(load_markdown_folder("data"))

@app.get("/health")
def health():
    return {"status": "ok", "documents": len(retriever.documents)}

@app.get("/search")
def search(q: str = Query(min_length=2), limit: int = Query(default=3, ge=1, le=10)):
    hits = retriever.search(q, limit)
    return {"query": q, "results": hits}
