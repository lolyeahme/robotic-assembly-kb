#!/usr/bin/env python3
"""Build Parent-Child JSONL chunks and SQLite Hybrid Search DB (FTS5 BM25 + TF-IDF RRF)
from Markdown files in kb/.

Usage:
    python3 etl/build_kb_index.py
"""
from __future__ import annotations

import json
import math
import re
import sqlite3
from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple

BASE_DIR = Path(__file__).resolve().parent.parent
KB_DIR = BASE_DIR / "kb"
JSONL_PATH = KB_DIR / "chunks_parent_child.jsonl"
DB_PATH = KB_DIR / "robotic_assembly_kb.db"

DOMAIN_KEYWORDS: Dict[str, List[str]] = {
    "sensing": ["vision", "mvs", "mvsnet", "pointflow", "gelsight", "tactile", "visuotactile", "视觉", "触觉", "传感", "点云"],
    "sim2real": ["sim2real", "fem", "ipc", "domain randomization", "仿真", "域随机化", "迁移"],
    "compliance_control": ["rcc", "compliance", "accommodation", "impedance", "hc-cps", "jamming", "force", "柔顺", "阻抗", "卡滞", "力控"],
    "pih_mechanics": ["peg-in-hole", "pih", "screw", "dual", "clearance", "interference", "轴孔", "螺旋", "双轴孔", "过盈", "间隙"],
    "learning_rl": ["lfd", "lfe", "gpr", "rl", "ddpg", "mddpg", "td3", "dqn", "hrl", "gvf", "vtsp", "vae", "gmr", "强化学习", "示教"],
    "dfa_design": ["dfa", "chamfer", "snap-fit", "layered", "ipa", "倒角", "卡扣", "面向装配", "设计"],
    "programming": ["val-ii", "rail", "srl", "arl", "rodabas", "fa-basic", "mcp", "编程", "语言", "世界模型"],
    "robots_systems": ["scara", "pragma", "yesman", "asea", "ibm", "hitachi", "flymo", "saab", "flair", "机器人", "产线"],
    "economics": ["economics", "miller", "boothroyd", "redford", "breakeven", "cost", "feeder", "经济", "成本", "供料", "盈亏平衡"],
}


def tokenize_bilingual(text: str) -> List[str]:
    """Bilingual tokenizer: preserves English/technical tokens (e.g. VA-Point-MVSNet, VAL-II)
    and generates CJK unigrams + bigrams for high-recall Chinese search."""
    tokens: List[str] = []
    # Technical / English tokens (keep hyphenated forms + split sub-parts)
    for m in re.finditer(r"[A-Za-z0-9]+(?:[-_/][A-Za-z0-9]+)*", text):
        tok = m.group(0).lower()
        tokens.append(tok)
        if "-" in tok or "_" in tok or "/" in tok:
            for part in re.split(r"[-_/]", tok):
                if len(part) >= 2:
                    tokens.append(part)
    # CJK characters -> unigrams + bigrams
    for seg in re.findall(r"[\u4e00-\u9fff]+", text):
        chars = list(seg)
        tokens.extend(chars)
        for i in range(len(chars) - 1):
            tokens.append(chars[i] + chars[i + 1])
    return tokens


def infer_book_meta(filename: str) -> Tuple[str, str]:
    name = filename.lower()
    if "2025" in name:
        return "book2025", "2025"
    if "1985" in name:
        return "book1985", "1985"
    if "glossary" in name:
        return "cross_era_glossary", "1985-2025"
    return "cross_era_synthesis", "1985-2025"


def infer_domain_tags(text: str) -> List[str]:
    lower = text.lower()
    tags = []
    for tag, kws in DOMAIN_KEYWORDS.items():
        if any(kw in lower for kw in kws):
            tags.append(tag)
    return tags or ["general"]


def infer_content_type(text: str) -> str:
    if "|" in text and "---" in text:
        return "table"
    if "$" in text or "\\frac" in text:
        return "formula_text"
    if "algorithm" in text.lower() or "伪代码" in text:
        return "algorithm"
    return "text"


def split_sections(md_text: str) -> List[Tuple[str, str]]:
    """Split a Markdown file by H2 (## ) sections."""
    lines = md_text.splitlines()
    sections: List[Tuple[str, str]] = []
    current_title = "Overview"
    buf: List[str] = []
    for line in lines:
        if line.startswith("## "):
            if buf:
                body = "\n".join(buf).strip()
                if body:
                    sections.append((current_title, body))
            current_title = line[3:].strip()
            buf = [line]
        else:
            buf.append(line)
    if buf:
        body = "\n".join(buf).strip()
        if body:
            sections.append((current_title, body))
    return sections


def split_children(section_title: str, section_body: str, max_chars: int = 750) -> List[str]:
    """Split a parent section into semantic child chunks while keeping tables intact."""
    blocks = re.split(r"\n\s*\n", section_body)
    chunks: List[str] = []
    cur: List[str] = []
    cur_len = 0
    for blk in blocks:
        blk = blk.strip()
        if not blk or blk == "---":
            continue
        # Keep markdown tables together as one chunk unless huge
        is_table = blk.startswith("|") and "\n|" in blk
        if is_table and len(blk) <= 2000:
            if cur:
                chunks.append("\n\n".join(cur))
                cur, cur_len = [], 0
            chunks.append(f"[{section_title}]\n{blk}")
            continue
        if cur_len + len(blk) > max_chars and cur:
            chunks.append("\n\n".join(cur))
            cur, cur_len = [blk], len(blk)
        else:
            cur.append(blk)
            cur_len += len(blk)
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks or [section_body]


def parse_glossary_rows(glossary_md: str) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for line in glossary_md.splitlines():
        if not line.strip().startswith("|"):
            continue
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) == 4 and not parts[0].startswith(":---") and not parts[0].startswith("---"):
            if parts[0] in ("缩略词", "术语 / 缩写", "技术领域"):
                continue
            term = re.sub(r"\*\*", "", parts[0]).strip()
            full_name = re.sub(r"\*\*", "", parts[1]).strip()
            definition = re.sub(r"\*\*", "", parts[2]).strip()
            source = re.sub(r"\*\*", "", parts[3]).strip()
            rows.append({
                "term": term,
                "full_name": full_name,
                "definition": definition,
                "source": source,
            })
    return rows


def build_index() -> None:
    md_files = sorted(KB_DIR.glob("*.md"))
    full_pages_dir = KB_DIR / "full_pages"
    if full_pages_dir.exists():
        md_files.extend(sorted(full_pages_dir.glob("*.md")))

    parents: List[Dict] = []
    children: List[Dict] = []
    glossary_rows: List[Dict[str, str]] = []

    p_counter = 0
    c_counter = 0

    for md_path in md_files:
        text = md_path.read_text(encoding="utf-8")
        book_id, year = infer_book_meta(md_path.name)
        rel_file = str(md_path.relative_to(BASE_DIR))

        if "glossary" in md_path.name.lower():
            glossary_rows.extend(parse_glossary_rows(text))

        for sec_title, sec_body in split_sections(text):
            p_counter += 1
            parent_id = f"P{p_counter:04d}"
            p_tags = infer_domain_tags(sec_title + "\n" + sec_body)
            parents.append({
                "parent_id": parent_id,
                "book_id": book_id,
                "year": year,
                "source_file": rel_file,
                "section_title": sec_title,
                "domain_tags": p_tags,
                "content": sec_body,
            })

            for idx, child_text in enumerate(split_children(sec_title, sec_body), start=1):
                c_counter += 1
                child_id = f"C{c_counter:05d}"
                c_tags = infer_domain_tags(sec_title + "\n" + child_text)
                ctype = infer_content_type(child_text)
                children.append({
                    "child_id": child_id,
                    "parent_id": parent_id,
                    "chunk_index": idx,
                    "book_id": book_id,
                    "year": year,
                    "source_file": rel_file,
                    "section_title": sec_title,
                    "domain_tags": c_tags,
                    "content_type": ctype,
                    "content": child_text,
                })

    # Write Parent-Child JSONL for RAGFlow / Dify / Vector DB ingestion
    with JSONL_PATH.open("w", encoding="utf-8") as f:
        for ch in children:
            f.write(json.dumps(ch, ensure_ascii=False) + "\n")

    # Compute TF-IDF vectors for zero-dependency hybrid retrieval
    doc_tokens = [tokenize_bilingual(c["section_title"] + " " + c["content"]) for c in children]
    df: Counter = Counter()
    for toks in doc_tokens:
        for t in set(toks):
            df[t] += 1
    n_docs = max(len(children), 1)
    idf: Dict[str, float] = {t: math.log((n_docs + 1) / (cnt + 1)) + 1.0 for t, cnt in df.items()}

    # Build SQLite DB
    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executescript("""
    CREATE TABLE parents (
        parent_id TEXT PRIMARY KEY,
        book_id TEXT NOT NULL,
        year TEXT NOT NULL,
        source_file TEXT NOT NULL,
        section_title TEXT NOT NULL,
        domain_tags TEXT NOT NULL,
        content TEXT NOT NULL
    );

    CREATE TABLE children (
        child_id TEXT PRIMARY KEY,
        parent_id TEXT NOT NULL,
        chunk_index INTEGER NOT NULL,
        book_id TEXT NOT NULL,
        year TEXT NOT NULL,
        source_file TEXT NOT NULL,
        section_title TEXT NOT NULL,
        domain_tags TEXT NOT NULL,
        content_type TEXT NOT NULL,
        content TEXT NOT NULL,
        tfidf_json TEXT NOT NULL,
        FOREIGN KEY (parent_id) REFERENCES parents(parent_id)
    );

    CREATE VIRTUAL TABLE children_fts USING fts5(
        child_id UNINDEXED,
        section_title,
        tokens_text,
        tokenize='unicode61'
    );

    CREATE TABLE vocab_idf (
        term TEXT PRIMARY KEY,
        idf REAL NOT NULL
    );

    CREATE TABLE glossary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        term TEXT NOT NULL,
        full_name TEXT NOT NULL,
        definition TEXT NOT NULL,
        source TEXT NOT NULL,
        search_tokens TEXT NOT NULL
    );
    """)

    for p in parents:
        cur.execute(
            "INSERT INTO parents VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                p["parent_id"], p["book_id"], p["year"], p["source_file"],
                p["section_title"], json.dumps(p["domain_tags"], ensure_ascii=False), p["content"],
            ),
        )

    for c, toks in zip(children, doc_tokens):
        tf = Counter(toks)
        total = max(len(toks), 1)
        vec = {t: (cnt / total) * idf[t] for t, cnt in tf.items()}
        norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
        vec_norm = {t: round(v / norm, 5) for t, v in vec.items()}
        tokens_text = " ".join(toks)

        cur.execute(
            "INSERT INTO children VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                c["child_id"], c["parent_id"], c["chunk_index"], c["book_id"], c["year"],
                c["source_file"], c["section_title"],
                json.dumps(c["domain_tags"], ensure_ascii=False),
                c["content_type"], c["content"], json.dumps(vec_norm, ensure_ascii=False),
            ),
        )
        cur.execute(
            "INSERT INTO children_fts VALUES (?, ?, ?)",
            (c["child_id"], c["section_title"], tokens_text),
        )

    cur.executemany("INSERT INTO vocab_idf VALUES (?, ?)", list(idf.items()))

    for g in glossary_rows:
        g_tokens = " ".join(tokenize_bilingual(f"{g['term']} {g['full_name']} {g['definition']}"))
        cur.execute(
            "INSERT INTO glossary (term, full_name, definition, source, search_tokens) VALUES (?, ?, ?, ?, ?)",
            (g["term"], g["full_name"], g["definition"], g["source"], g_tokens),
        )

    conn.commit()
    conn.close()
    print(f"[OK] Built KB index: {len(parents)} parent sections, {len(children)} child chunks, {len(glossary_rows)} glossary entries.")
    print(f"     JSONL -> {JSONL_PATH}")
    print(f"     SQLite -> {DB_PATH}")


if __name__ == "__main__":
    build_index()
