import re
from dataclasses import dataclass
from pathlib import Path
from typing import List

STOPWORDS = {"the", "and", "for", "with", "from", "that", "this", "are", "into", "your", "you"}

def tokens(text: str) -> set[str]:
    return {word for word in re.findall(r"[a-zA-Z0-9]+", text.lower()) if word not in STOPWORDS}

@dataclass
class Document:
    title: str
    text: str
    source: str

class Retriever:
    def __init__(self, documents: List[Document]):
        self.documents = documents

    def search(self, query: str, limit: int = 3) -> list[dict]:
        query_tokens = tokens(query)
        scored = []
        for doc in self.documents:
            doc_tokens = tokens(doc.text)
            overlap = query_tokens & doc_tokens
            score = len(overlap) / max(len(query_tokens), 1)
            scored.append({"title": doc.title, "source": doc.source, "text": doc.text, "score": round(score, 3)})
        return sorted(scored, key=lambda item: item["score"], reverse=True)[:limit]

def load_markdown_folder(folder: str) -> list[Document]:
    documents = []
    for path in sorted(Path(folder).glob("*.md")):
        text = path.read_text(encoding="utf-8")
        title = next((line.lstrip("# ").strip() for line in text.splitlines() if line.startswith("#")), path.stem)
        documents.append(Document(title=title, text=text, source=path.name))
    return documents
