#!/usr/bin/env python3
"""Optional Dense Vector Index Builder (BGE-M3 + ChromaDB).

Use this locally when you want dense multilingual semantic embeddings on top of
the built-in zero-dependency SQLite FTS5 BM25 + TF-IDF hybrid search.

Requirements:
    pip install chromadb sentence-transformers

Usage:
    python3 etl/build_vector_index.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
JSONL_PATH = BASE_DIR / "kb" / "chunks_parent_child.jsonl"
CHROMA_DIR = BASE_DIR / "kb" / "chroma_bge_m3"
MODEL_NAME = "BAAI/bge-m3"


def main() -> None:
    import chromadb
    from sentence_transformers import SentenceTransformer

    chunks = [json.loads(line) for line in JSONL_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
    print(f"Loaded {len(chunks)} chunks from {JSONL_PATH}")

    model = SentenceTransformer(MODEL_NAME)
    texts = [f"{c['section_title']}\n{c['content']}" for c in chunks]
    embeddings = model.encode(texts, normalize_embeddings=True, show_progress_bar=True).tolist()

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    try:
        client.delete_collection("robotic_assembly_kb")
    except Exception:
        pass
    col = client.create_collection(name="robotic_assembly_kb", metadata={"hnsw:space": "cosine"})

    col.add(
        ids=[c["child_id"] for c in chunks],
        documents=texts,
        embeddings=embeddings,
        metadatas=[
            {
                "parent_id": c["parent_id"],
                "book_id": c["book_id"],
                "year": c["year"],
                "section_title": c["section_title"],
                "domain_tags": ",".join(c["domain_tags"]),
                "content_type": c["content_type"],
                "source_file": c["source_file"],
            }
            for c in chunks
        ],
    )
    print(f"[OK] Built ChromaDB BGE-M3 index at {CHROMA_DIR} ({col.count()} vectors).")


if __name__ == "__main__":
    main()
