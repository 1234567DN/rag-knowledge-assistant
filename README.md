# RAG Knowledge Assistant

A compact retrieval-augmented generation foundation that indexes Markdown knowledge, ranks relevant context with transparent lexical scoring, and exposes results through a FastAPI endpoint.

## What it demonstrates

- Document ingestion from a folder
- Query tokenization and relevance scoring
- Source-aware search results for downstream LLM prompting
- FastAPI interface suitable for a Lovable, React, or n8n client
- Test coverage for retrieval behavior

The retrieval layer is intentionally dependency-light so it is easy to understand and extend with embeddings or a hosted vector database later.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.api:app --reload
```

Then query the knowledge base:

```bash
curl 'http://127.0.0.1:8000/search?q=agent%20task%20routing'
```

Run tests with `pytest`.
