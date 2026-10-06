import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
from src.rag import Document, Retriever

def test_retriever_prioritizes_relevant_document():
    retriever = Retriever([
        Document("AI", "agent routing and task history", "ai.md"),
        Document("Database", "supabase row-level security and realtime", "db.md"),
    ])
    results = retriever.search("agent task routing")
    assert results[0]["title"] == "AI"
    assert results[0]["score"] > 0
