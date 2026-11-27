#!/usr/bin/env python3
"""Standard Model Context Protocol (MCP) stdio server for the Robotic Assembly Knowledge Base.

Zero external dependencies (Python 3 stdlib only). Compatible with:
- Claude Desktop / Claude Code
- Cursor / Windsurf / Cline
- Gemini CLI & any MCP-compliant Agent

Run directly:
    python3 servers/mcp_server.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict

# Ensure sibling imports work regardless of CWD
sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_engine import RoboticAssemblyKB

SERVER_INFO = {
    "name": "robotic-assembly-kb",
    "version": "1.0.0",
}

TOOLS = [
    {
        "name": "search_kb",
        "description": (
            "Hybrid search (BM25 + TF-IDF RRF + Parent-Child expansion) across both "
            "'Robotic Intelligent Assembly' (2025) and 'Robotic Assembly' (1985), plus cross-era matrices. "
            "Supports Chinese and English queries and optional filtering by book_id, year, or domain_tag."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query in Chinese or English"},
                "top_k": {"type": "integer", "default": 5, "description": "Number of top results (1-15)"},
                "book_id": {
                    "type": "string",
                    "enum": ["book2025", "book1985", "cross_era_glossary", "cross_era_synthesis"],
                    "description": "Optional filter by book or cross-era document",
                },
                "year": {"type": "string", "description": "Optional year filter: '1985' or '2025'"},
                "domain_tag": {
                    "type": "string",
                    "description": "Optional domain filter: sensing, sim2real, compliance_control, pih_mechanics, learning_rl, dfa_design, programming, robots_systems, economics",
                },
                "include_parent": {"type": "boolean", "default": True, "description": "Return full parent section context"},
            },
            "required": ["query"],
        },
    },
    {
        "name": "get_parent_section",
        "description": "Fetch the full parent section by parent_id (e.g., P0005) returned from search_kb or list_kb_structure.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "parent_id": {"type": "string", "description": "Parent section ID, e.g. P0005"},
            },
            "required": ["parent_id"],
        },
    },
    {
        "name": "lookup_glossary",
        "description": "Look up acronyms, technical terms, and 1985-to-2025 cross-era mappings (e.g. RCC, HC-CPS, VA-Point-MVSNet, RODABAS, DFA).",
        "inputSchema": {
            "type": "object",
            "properties": {
                "term": {"type": "string", "description": "Acronym or term to look up"},
                "limit": {"type": "integer", "default": 8},
            },
            "required": ["term"],
        },
    },
    {
        "name": "list_kb_structure",
        "description": "List all chapters, parts, sections, parent_ids, and statistics in the Robotic Assembly Knowledge Base.",
        "inputSchema": {
            "type": "object",
            "properties": {},
        },
    },
]


def send_message(msg: Dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(msg, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def handle_request(kb: RoboticAssemblyKB, req: Dict[str, Any]) -> Dict[str, Any] | None:
    req_id = req.get("id")
    method = req.get("method", "")
    params = req.get("params") or {}

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": SERVER_INFO,
            },
        }
    if method == "notifications/initialized":
        return None
    if method == "ping":
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS}}
    if method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments") or {}
        try:
            if tool_name == "search_kb":
                data = kb.search(
                    query=args["query"],
                    top_k=int(args.get("top_k", 5)),
                    book_id=args.get("book_id"),
                    year=args.get("year"),
                    domain_tag=args.get("domain_tag"),
                    include_parent=bool(args.get("include_parent", True)),
                )
            elif tool_name == "get_parent_section":
                data = kb.get_parent_section(args["parent_id"])
            elif tool_name == "lookup_glossary":
                data = kb.lookup_glossary(args["term"], limit=int(args.get("limit", 8)))
            elif tool_name == "list_kb_structure":
                data = kb.list_structure()
            else:
                return {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"},
                }
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(data, ensure_ascii=False, indent=2)}],
                    "isError": False,
                },
            }
        except Exception as exc:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": f"Error: {exc}"}],
                    "isError": True,
                },
            }

    if req_id is not None:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": -32601, "message": f"Method not found: {method}"},
        }
    return None


def main() -> None:
    kb = RoboticAssemblyKB()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue
        resp = handle_request(kb, req)
        if resp is not None:
            send_message(resp)


if __name__ == "__main__":
    main()
