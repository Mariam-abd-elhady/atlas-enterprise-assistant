"""Session memory keyed by session_id. Owner: Person 2."""


def load_history(session_id: str) -> list[dict]:
    """Return all previous turns for this session (empty for a new session)."""
    raise NotImplementedError


def save_turn(session_id: str, question: str, answer: str) -> None:
    """Append one question/answer pair to the session."""
    raise NotImplementedError


def clear_session(session_id: str) -> None:
    """Forget a session (used by the New chat button)."""
    raise NotImplementedError
