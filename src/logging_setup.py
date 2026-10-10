"""Structured JSON logging. Owner: Person 3."""


def new_run_id() -> str:
    """Return a fresh UUID string for one question."""
    raise NotImplementedError


def log_event(run_id: str, event: str, **data) -> None:
    """Append one JSON line to RUN_LOG_PATH. Log filenames/chunk IDs, not full text."""
    raise NotImplementedError
