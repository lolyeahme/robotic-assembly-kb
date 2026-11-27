#!/usr/bin/env python3
"""Run automated retrieval evaluation (Recall@1, Recall@3, Recall@5, MRR) on golden_qa.jsonl."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "servers"))
from kb_engine import RoboticAssemblyKB


def main() -> None:
    kb = RoboticAssemblyKB()
    qa_path = BASE_DIR / "eval" / "golden_qa.jsonl"
    cases = [json.loads(line) for line in qa_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    r1 = r3 = r5 = 0
    mrr_sum = 0.0
    failures = []

    for case in cases:
        hits = kb.search(case["query"], top_k=5, include_parent=True)
        kws = [k.lower() for k in case["expected_keywords"]]
        first_rank = None
        for idx, h in enumerate(hits, start=1):
            haystack = (h["section_title"] + "\n" + h["matched_chunk"] + "\n" + h.get("parent_context", "")).lower()
            if all(kw in haystack for kw in kws):
                first_rank = idx
                break
        if first_rank is not None:
            if first_rank <= 1:
                r1 += 1
            if first_rank <= 3:
                r3 += 1
            if first_rank <= 5:
                r5 += 1
            mrr_sum += 1.0 / first_rank
        else:
            failures.append((case["id"], case["query"], [h["section_title"] for h in hits[:3]]))

    n = len(cases)
    print(f"=== Robotic Assembly KB Retrieval Evaluation ({n} queries) ===")
    print(f"Recall@1 : {r1}/{n} ({r1 / n * 100:.1f}%)")
    print(f"Recall@3 : {r3}/{n} ({r3 / n * 100:.1f}%)")
    print(f"Recall@5 : {r5}/{n} ({r5 / n * 100:.1f}%)")
    print(f"MRR@5    : {mrr_sum / n:.4f}")
    if failures:
        print("\nMissed queries:")
        for qid, q, titles in failures:
            print(f"  - {qid}: {q} -> top3={titles}")
        sys.exit(1)
    print("\n[PASS] All golden evaluation queries hit expected evidence within Top-5.")


if __name__ == "__main__":
    main()
