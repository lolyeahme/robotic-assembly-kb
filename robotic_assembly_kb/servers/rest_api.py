#!/usr/bin/env python3
"""Cloud-Ready FastAPI REST + OpenAPI + Remote MCP (Streamable HTTP) server.

Features:
- Bearer Token / X-API-Key authentication via environment variable KB_API_KEY
- OpenAPI 3.1 schema with HTTPBearer security for ChatGPT Custom GPT Actions, Dify, LangChain, CrewAI
- Remote MCP Streamable HTTP endpoint (POST /mcp) for Claude, Cursor, Windsurf, Gemini CLI
- Health probe endpoint (/health) for Google Cloud Run and Render

Run locally:
    KB_API_KEY=my-secret-key uvicorn servers.rest_api:app --host 0.0.0.0 --port 8080
"""
from __future__ import annotations

import hmac
import os
import sys
from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import Depends, FastAPI, Header, HTTPException, Query, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_engine import RoboticAssemblyKB
from mcp_server import handle_request as handle_mcp_request

kb = RoboticAssemblyKB()
bearer_scheme = HTTPBearer(auto_error=False)


def verify_api_key(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(bearer_scheme),
    x_api_key: Optional[str] = Header(default=None, alias="X-API-Key"),
) -> None:
    """Enforce Bearer / X-API-Key auth whenever KB_API_KEY env var is non-empty."""
    expected = os.environ.get("KB_API_KEY", "").strip()
    if not expected:
        return  # Local dev mode (no key configured)

    provided = credentials.credentials if credentials else (x_api_key or "")
    if not provided or not hmac.compare_digest(provided, expected):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key. Provide 'Authorization: Bearer <KB_API_KEY>' or 'X-API-Key'.",
            headers={"WWW-Authenticate": "Bearer"},
        )


app = FastAPI(
    title="Robotic Assembly Knowledge Base API (1985-2025)",
    description=(
        "Cloud-ready engineering hybrid search API & Remote MCP server over "
        "'Robotic Intelligent Assembly' (2025) and 'Robotic Assembly' (1985), "
        "with Parent-Child context expansion and cross-era glossary."
    ),
    version="1.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class SearchRequest(BaseModel):
    query: str = Field(..., description="Query in Chinese or English")
    top_k: int = Field(5, ge=1, le=20)
    book_id: Optional[str] = Field(None, description="book2025 | book1985 | cross_era_glossary | cross_era_synthesis")
    year: Optional[str] = Field(None, description="1985 or 2025")
    domain_tag: Optional[str] = Field(
        None,
        description="e.g. compliance_control, sensing, sim2real, pih_mechanics, learning_rl, dfa_design, programming, robots_systems, economics",
    )
    include_parent: bool = Field(True, description="Include full parent section context")


@app.get("/health", tags=["System"])
def health() -> Dict[str, Any]:
    """Unauthenticated health probe for Cloud Run / Render."""
    return {
        "status": "ok",
        "auth_enabled": bool(os.environ.get("KB_API_KEY", "").strip()),
        "stats": kb.list_structure()["stats"],
    }


@app.post("/search", dependencies=[Depends(verify_api_key)], tags=["Knowledge Base"])
def search_post(req: SearchRequest) -> Dict[str, Any]:
    hits = kb.search(
        query=req.query,
        top_k=req.top_k,
        book_id=req.book_id,
        year=req.year,
        domain_tag=req.domain_tag,
        include_parent=req.include_parent,
    )
    return {"query": req.query, "count": len(hits), "results": hits}


@app.get("/search", dependencies=[Depends(verify_api_key)], tags=["Knowledge Base"])
def search_get(
    q: str = Query(..., description="Query string"),
    top_k: int = Query(5, ge=1, le=20),
    book_id: Optional[str] = None,
    year: Optional[str] = None,
    domain_tag: Optional[str] = None,
    include_parent: bool = True,
) -> Dict[str, Any]:
    hits = kb.search(
        query=q,
        top_k=top_k,
        book_id=book_id,
        year=year,
        domain_tag=domain_tag,
        include_parent=include_parent,
    )
    return {"query": q, "count": len(hits), "results": hits}


@app.get("/sections/{parent_id}", dependencies=[Depends(verify_api_key)], tags=["Knowledge Base"])
def get_section(parent_id: str) -> Dict[str, Any]:
    sec = kb.get_parent_section(parent_id)
    if not sec:
        raise HTTPException(status_code=404, detail=f"Section {parent_id} not found")
    return sec


@app.get("/glossary", dependencies=[Depends(verify_api_key)], tags=["Knowledge Base"])
def lookup_glossary(term: str = Query(..., description="Term or acronym"), limit: int = 10) -> Dict[str, Any]:
    items = kb.lookup_glossary(term, limit=limit)
    return {"term": term, "count": len(items), "entries": items}


@app.get("/structure", dependencies=[Depends(verify_api_key)], tags=["Knowledge Base"])
def list_structure() -> Dict[str, Any]:
    return kb.list_structure()


@app.post("/mcp", dependencies=[Depends(verify_api_key)], tags=["Remote MCP"])
async def mcp_http_endpoint(request: Request) -> Response:
    """Remote MCP Streamable HTTP (JSON-RPC 2.0) endpoint.

    Supports initialize, notifications/initialized, ping, tools/list, and tools/call.
    """
    import json

    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON-RPC payload")

    # Support both single request and JSON-RPC batch
    if isinstance(payload, list):
        responses = []
        for item in payload:
            r = handle_mcp_request(kb, item)
            if r is not None:
                responses.append(r)
        if not responses:
            return Response(status_code=202)
        return Response(content=json.dumps(responses, ensure_ascii=False), media_type="application/json")

    resp = handle_mcp_request(kb, payload)
    if resp is None:
        return Response(status_code=202)
    return Response(content=json.dumps(resp, ensure_ascii=False), media_type="application/json")
