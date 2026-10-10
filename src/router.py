"""Question router (hr / it / finance). Owner: Person 2."""


def route(question: str, history: list[dict] | None = None) -> tuple[str, float]:
    """Classify a question.

    Args:
        question: Current user question.
        history: Previous turns, so follow-ups resolve.
    Returns:
        (domain, confidence). Low confidence triggers the fallback in graph.py.
    """
    raise NotImplementedError
