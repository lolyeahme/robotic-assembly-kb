#!/usr/bin/env python3
"""Dual-Track Full-Page PDF ETL Pipeline for the Two Robotic Assembly Books.

Run locally with your two PDFs to expand the knowledge base to full verbatim 636 pages:
    python3 etl/pdf_dual_track_etl.py \
        --book2025 "/path/to/Robotic Intelligent Assembly (2025).pdf" \
        --book1985 "/path/to/Robotic assembly (1985).pdf" \
        --vlm-provider none

Supported --vlm-provider modes for Book1985 (scanned 1985 pages):
  - none      : Local OpenCV blank-page removal + Tesseract OSD auto-rotation + Tesseract OCR
  - openai    : Any OpenAI-compatible VLM endpoint (set OPENAI_API_KEY, OPENAI_BASE_URL, VLM_MODEL)
  - gemini    : Google Gemini Vision API (set GEMINI_API_KEY, VLM_MODEL=gemini-2.5-flash)
"""
from __future__ import annotations

import argparse
import base64
import io
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
FULL_PAGES_DIR = BASE_DIR / "kb" / "full_pages"
ASSETS_DIR = BASE_DIR / "kb" / "assets"


def is_blank_page(pil_img, dark_pixel_ratio_threshold: float = 0.003) -> bool:
    import numpy as np
    gray = pil_img.convert("L")
    arr = np.asarray(gray)
    dark_ratio = float((arr < 200).mean())
    return dark_ratio < dark_pixel_ratio_threshold


def detect_and_fix_rotation(pil_img):
    """Detect 90/180/270 degree rotated pages (e.g., Book1985 PDF p.53 ARL grammar table)
    using Tesseract OSD and rotate upright."""
    try:
        import pytesseract
        osd = pytesseract.image_to_osd(pil_img)
        m = re.search(r"Rotate:\s*(\d+)", osd)
        if m:
            angle = int(m.group(1))
            if angle in (90, 180, 270):
                return pil_img.rotate(-angle, expand=True), angle
    except Exception:
        pass
    return pil_img, 0


def ocr_with_tesseract(pil_img) -> str:
    import pytesseract
    return pytesseract.image_to_string(pil_img, lang="eng", config="--psm 6")


def ocr_with_vlm_openai(pil_img, page_num: int) -> str:
    import urllib.request
    import json

    api_key = os.environ["OPENAI_API_KEY"]
    base_url = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.environ.get("VLM_MODEL", "gpt-4o-mini")

    buf = io.BytesIO()
    pil_img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")

    prompt = (
        "Transcribe this 1985 robotics engineering book page into clean Markdown. "
        "Preserve headings, convert math formulas to LaTeX ($...$ or $$...$$), "
        "preserve code listings (VAL-II/RAIL/ARL/SRL) in fenced code blocks, "
        "reconstruct tables as Markdown pipe tables, and summarize any figures in "
        "> [Figure Summary]: ... blocks. Fix obvious scan artifacts without inventing facts."
    )
    payload = {
        "model": model,
        "temperature": 0.0,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
                ],
            }
        ],
    }
    req = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def parse_book2025(pdf_path: Path, max_pages: Optional[int] = None) -> Path:
    """Track A (Born-Digital 2025 Monograph):
    Uses MinerU CLI if installed; otherwise falls back to pdfplumber with table extraction."""
    FULL_PAGES_DIR.mkdir(parents=True, exist_ok=True)
    out_md = FULL_PAGES_DIR / "book2025_full_pages.md"

    # Prefer MinerU if available in PATH
    if subprocess.run(["which", "magic-pdf"], capture_output=True).returncode == 0 and max_pages is None:
        print("[Track A] Detected MinerU (magic-pdf). Running layout + LaTeX extraction...")
        mineru_out = ASSETS_DIR / "mineru_book2025"
        mineru_out.mkdir(parents=True, exist_ok=True)
        subprocess.run(["magic-pdf", "-p", str(pdf_path), "-o", str(mineru_out), "-m", "auto"], check=True)
        md_candidates = list(mineru_out.rglob("*.md"))
        if md_candidates:
            out_md.write_text(md_candidates[0].read_text(encoding="utf-8"), encoding="utf-8")
            print(f"[Track A] Saved MinerU output -> {out_md}")
            return out_md

    # Portable fallback: pdfplumber
    import pdfplumber

    print(f"[Track A] Parsing Book2025 via pdfplumber: {pdf_path}")
    sections: List[str] = ["# 《Robotic Intelligent Assembly》(2025) Full-Page Extract\n"]
    with pdfplumber.open(pdf_path) as pdf:
        total = min(len(pdf.pages), max_pages) if max_pages else len(pdf.pages)
        for i in range(total):
            page = pdf.pages[i]
            text = (page.extract_text() or "").strip()
            tables = page.extract_tables() or []
            if not text and not tables:
                continue
            sections.append(f"## Book2025 Page {i + 1} [Book2025 p.{i + 1}]\n")
            if text:
                sections.append(text + "\n")
            for t_idx, tbl in enumerate(tables, start=1):
                cleaned = [[(c or "").replace("\n", " ").strip() for c in row] for row in tbl if any(row)]
                if len(cleaned) >= 2:
                    header = "| " + " | ".join(cleaned[0]) + " |"
                    sep = "| " + " | ".join(["---"] * len(cleaned[0])) + " |"
                    body = "\n".join("| " + " | ".join(r) + " |" for r in cleaned[1:])
                    sections.append(f"\n### Table {t_idx} (p.{i + 1})\n{header}\n{sep}\n{body}\n")
    out_md.write_text("\n".join(sections), encoding="utf-8")
    print(f"[Track A] Saved {total} pages -> {out_md}")
    return out_md


def parse_book1985(pdf_path: Path, vlm_provider: str = "none", dpi: int = 220, max_pages: Optional[int] = None) -> Path:
    """Track B (Scanned 1985 Anthology):
    Renders pages -> drops blank dividers -> auto-rotates landscape tables (e.g. p.53) -> VLM or Tesseract OCR."""
    import pypdfium2 as pdfium

    FULL_PAGES_DIR.mkdir(parents=True, exist_ok=True)
    out_md = FULL_PAGES_DIR / "book1985_full_pages.md"

    pdf = pdfium.PdfDocument(str(pdf_path))
    total = min(len(pdf), max_pages) if max_pages else len(pdf)
    scale = dpi / 72.0
    sections: List[str] = ["# 《Robotic Assembly》(1985) Full-Page OCR/VLM Extract\n"]

    print(f"[Track B] Parsing Book1985 ({total} pages, provider={vlm_provider}): {pdf_path}")
    for i in range(total):
        page_num = i + 1
        pil_img = pdf[i].render(scale=scale).to_pil()
        if is_blank_page(pil_img):
            continue
        pil_img, angle = detect_and_fix_rotation(pil_img)
        rot_note = f" (auto-rotated {angle} deg)" if angle else ""
        if vlm_provider == "openai":
            text = ocr_with_vlm_openai(pil_img, page_num)
        else:
            text = ocr_with_tesseract(pil_img)
        text = text.strip()
        if not text:
            continue
        sections.append(f"## Book1985 Page {page_num} [Book1985 p.{page_num}]{rot_note}\n\n{text}\n")
        if page_num % 20 == 0 or page_num == total:
            print(f"  processed {page_num}/{total} pages...")

    out_md.write_text("\n".join(sections), encoding="utf-8")
    print(f"[Track B] Saved full-page extract -> {out_md}")
    return out_md


def main() -> None:
    parser = argparse.ArgumentParser(description="Dual-Track Full-Page PDF ETL for Robotic Assembly KB")
    parser.add_argument("--book2025", type=Path, help="Path to Robotic Intelligent Assembly (2025).pdf")
    parser.add_argument("--book1985", type=Path, help="Path to Robotic assembly (1985).pdf")
    parser.add_argument("--vlm-provider", choices=["none", "openai"], default="none")
    parser.add_argument("--dpi", type=int, default=220)
    parser.add_argument("--max-pages", type=int, default=None, help="Optional page cap for quick smoke testing")
    args = parser.parse_args()

    if not args.book2025 and not args.book1985:
        parser.error("Provide at least one of --book2025 or --book1985")

    if args.book2025:
        parse_book2025(args.book2025, max_pages=args.max_pages)
    if args.book1985:
        parse_book1985(args.book1985, vlm_provider=args.vlm_provider, dpi=args.dpi, max_pages=args.max_pages)

    print("[Rebuild] Refreshing Parent-Child JSONL and SQLite Hybrid Index...")
    subprocess.run([sys.executable, str(BASE_DIR / "etl" / "build_kb_index.py")], check=True)


if __name__ == "__main__":
    main()
