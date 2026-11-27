#!/usr/bin/env python3
"""Zero-dependency Hybrid Search Engine for the Robotic Assembly Knowledge Base.

Combines:
1. SQLite FTS5 BM25 lexical ranking (bilingual English + CJK bigram tokenized)
2. Sparse TF-IDF Cosine similarity
3. Reciprocal Rank Fusion (RRF) + metadata filtering + Parent-Child context expansion
"""
from __future__ import annotations

import json
import math
import re
import sqlite3
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DB_PATH = BASE_DIR / "kb" / "robotic_assembly_kb.db"


def tokenize_bilingual(text: str) -> List[str]:
    tokens: List[str] = []
    for m in re.finditer(r"[A-Za-z0-9]+(?:[-_/][A-Za-z0-9]+)*", text):
        tok = m.group(0).lower()
        tokens.append(tok)
        if "-" in tok or "_" in tok or "/" in tok:
            for part in re.split(r"[-_/]", tok):
                if len(part) >= 2:
                    tokens.append(part)
    for seg in re.findall(r"[\u4e00-\u9fff]+", text):
        chars = list(seg)
        tokens.extend(chars)
        for i in range(len(chars) - 1):
            tokens.append(chars[i] + chars[i + 1])
    return tokens


class RoboticAssemblyKB:
    def __init__(self, db_path: Path | str = DEFAULT_DB_PATH):
        self.db_path = Path(db_path)
        if not self.db_path.exists():
            raise FileNotFoundError(f"KB database not found at {self.db_path}. Run etl/build_kb_index.py first.")
        self._idf_cache: Optional[Dict[str, float]] = None

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _get_idf(self, conn: sqlite3.Connection) -> Dict[str, float]:
        if self._idf_cache is None:
            rows = conn.execute("SELECT term, idf FROM vocab_idf").fetchall()
            self._idf_cache = {r["term"]: r["idf"] for r in rows}
        return self._idf_cache

    def search(
        self,
        query: str,
        top_k: int = 5,
        book_id: Optional[str] = None,
        year: Optional[str] = None,
        domain_tag: Optional[str] = None,
        include_parent: bool = True,
    ) -> List[Dict[str, Any]]:
        q_tokens = tokenize_bilingual(query)
        if not q_tokens:
            return []

        conn = self._connect()
        try:
            # 1) Filter candidate children by metadata
            where_clauses: List[str] = []
            params: List[Any] = []
            if book_id:
                where_clauses.append("c.book_id = ?")
                params.append(book_id)
            if year:
                where_clauses.append("c.year LIKE ?")
                params.append(f"%{year}%")
            if domain_tag:
                where_clauses.append("c.domain_tags LIKE ?")
                params.append(f'%"{domain_tag}"%')
            where_sql = ("WHERE " + " AND ".join(where_clauses)) if where_clauses else ""

            rows = conn.execute(
                f"SELECT c.child_id, c.parent_id, c.book_id, c.year, c.source_file, "
                f"c.section_title, c.domain_tags, c.content_type, c.content, c.tfidf_json "
                f"FROM children c {where_sql}",
                params,
            ).fetchall()
            if not rows:
                return []

            cand_map = {r["child_id"]: dict(r) for r in rows}

            # 2) FTS5 BM25 ranking
            fts_terms = [t for t in dict.fromkeys(q_tokens) if len(t) >= 1][:24]
            fts_query = " OR ".join(f'"{t.replace(chr(34), "")}"' for t in fts_terms)
            bm25_ranks: Dict[str, int] = {}
            try:
                fts_rows = conn.execute(
                    "SELECT child_id, bm25(children_fts) AS score "
                    "FROM children_fts WHERE children_fts MATCH ? ORDER BY score LIMIT 50",
                    (fts_query,),
                ).fetchall()
                rank = 0
                for r in fts_rows:
                    if r["child_id"] in cand_map:
                        rank += 1
                        bm25_ranks[r["child_id"]] = rank
            except sqlite3.OperationalError:
                pass

            # 3) Sparse TF-IDF cosine ranking
            idf = self._get_idf(conn)
            q_tf = Counter(q_tokens)
            q_total = len(q_tokens)
            q_vec = {t: (cnt / q_total) * idf.get(t, 1.0) for t, cnt in q_tf.items() if t in idf}
            q_norm = math.sqrt(sum(v * v for v in q_vec.values())) or 1.0
            q_vec = {t: v / q_norm for t, v in q_vec.items()}

            cos_scores: List[tuple[str, float]] = []
            for cid, row in cand_map.items():
                doc_vec = json.loads(row["tfidf_json"])
                dot = sum(qv * doc_vec.get(t, 0.0) for t, qv in q_vec.items())
                if dot > 0:
                    cos_scores.append((cid, dot))
            cos_scores.sort(key=lambda x: x[1], reverse=True)
            cos_ranks = {cid: idx + 1 for idx, (cid, _) in enumerate(cos_scores[:50])}

            # 4) Reciprocal Rank Fusion (RRF)
            rrf_k = 60.0
            fused: List[tuple[str, float]] = []
            all_ids = set(bm25_ranks.keys()) | set(cos_ranks.keys())
            for cid in all_ids:
                score = 0.0
                if cid in bm25_ranks:
                    score += 1.0 / (rrf_k + bm25_ranks[cid])
                if cid in cos_ranks:
                    score += 1.0 / (rrf_k + cos_ranks[cid])
                fused.append((cid, score))
            fused.sort(key=lambda x: x[1], reverse=True)

            results: List[Dict[str, Any]] = []
            for cid, score in fused[:top_k]:
                item = cand_map[cid]
                res: Dict[str, Any] = {
                    "child_id": cid,
                    "parent_id": item["parent_id"],
                    "score": round(score, 5),
                    "book_id": item["book_id"],
                    "year": item["year"],
                    "source_file": item["source_file"],
                    "section_title": item["section_title"],
                    "domain_tags": json.loads(item["domain_tags"]),
                    "content_type": item["content_type"],
                    "matched_chunk": item["content"],
                }
                if include_parent:
                    p_row = conn.execute(
                        "SELECT content FROM parents WHERE parent_id = ?",
                        (item["parent_id"],),
                    ).fetchone()
                    if p_row:
                        res["parent_context"] = p_row["content"]
                results.append(res)
            return results
        finally:
            conn.close()

    def get_parent_section(self, parent_id: str) -> Optional[Dict[str, Any]]:
        conn = self._connect()
        try:
            row = conn.execute("SELECT * FROM parents WHERE parent_id = ?", (parent_id,)).fetchone()
            if not row:
                return None
            d = dict(row)
            d["domain_tags"] = json.loads(d["domain_tags"])
            return d
        finally:
            conn.close()

    def lookup_glossary(self, query: str, limit: int = 10) -> List[Dict[str, str]]:
        q_lower = query.strip().lower()
        q_tokens = set(tokenize_bilingual(query))
        conn = self._connect()
        try:
            rows = conn.execute("SELECT term, full_name, definition, source, search_tokens FROM glossary").fetchall()
            scored = []
            for r in rows:
                score = 0
                if q_lower == r["term"].lower():
                    score += 100
                elif q_lower in r["term"].lower() or q_lower in r["full_name"].lower():
                    score += 50
                elif q_lower in r["definition"].lower():
                    score += 25
                row_tokens = set(r["search_tokens"].split())
                overlap = len(q_tokens & row_tokens)
                score += overlap * 5
                if score > 0:
                    scored.append((score, {
                        "term": r["term"],
                        "full_name": r["full_name"],
                        "definition": r["definition"],
                        "source": r["source"],
                    }))
            scored.sort(key=lambda x: x[0], reverse=True)
            return [item for _, item in scored[:limit]]
        finally:
            conn.close()

    def list_structure(self) -> Dict[str, Any]:
        conn = self._connect()
        try:
            p_rows = conn.execute(
                "SELECT parent_id, book_id, year, section_title, domain_tags FROM parents ORDER BY parent_id"
            ).fetchall()
            c_cnt = conn.execute("SELECT COUNT(*) FROM children").fetchone()[0]
            g_cnt = conn.execute("SELECT COUNT(*) FROM glossary").fetchone()[0]
            return {
                "stats": {
                    "parent_sections": len(p_rows),
                    "child_chunks": c_cnt,
                    "glossary_entries": g_cnt,
                },
                "sections": [
                    {
                        "parent_id": r["parent_id"],
                        "book_id": r["book_id"],
                        "year": r["year"],
                        "section_title": r["section_title"],
                        "domain_tags": json.loads(r["domain_tags"]),
                    }
                    for r in p_rows
                ],
            }
        finally:
            conn.close()
