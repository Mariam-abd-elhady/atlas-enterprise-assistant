"""Structured JSON logging. Owner: Person 3."""
import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path

RUN_LOG_PATH = os.getenv("RUN_LOG_PATH", "outputs/run_log.jsonl")


def new_run_id() -> str:
    """Return a fresh UUID string for one question."""
    return str(uuid.uuid4())


def chunk_metadata(chunk) -> dict:
    """Return loggable info for a retrieved chunk (filename/IDs only, not full text).

    Accepts a LangChain Document, an object with .metadata, or a plain dict.
    """
    if isinstance(chunk, dict):
        meta = chunk.get("metadata", chunk)
    else:
        meta = getattr(chunk, "metadata", {}) or {}
    return {
        "source": meta.get("source") or meta.get("filename"),
        "domain": meta.get("domain"),
        "chunk_id": meta.get("chunk_id") or meta.get("id"),
        "page": meta.get("page"),
    }


def log_event(run_id: str, event: str, **data) -> None:
    """Append one JSON line to RUN_LOG_PATH. Log filenames/chunk IDs, not full text."""
    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "run_id": run_id,
        "event": event,
        **data,
    }
    path = Path(RUN_LOG_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
