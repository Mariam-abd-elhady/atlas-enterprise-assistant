
"""Question router for HR, IT, and Finance domains."""

import re

DOMAIN_KEYWORDS = {
    "hr": {
        "leave", "vacation", "holiday", "employee", "employees",
        "attendance", "absence", "salary", "payroll", "recruitment",
        "resignation", "benefit", "insurance", "human resources",
        "annual leave", "sick leave",
    },
    "it": {
        "computer", "laptop", "software", "hardware", "network",
        "internet", "password", "login", "email", "printer",
        "system", "server", "bug", "access", "vpn", "permissions",
        "technical support", "troubleshooting",
    },
    "finance": {
        "invoice", "reimbursement", "expense", "budget", "payment",
        "refund", "purchase", "cost", "financial", "tax", "receipt",
        "expenses", "accounting", "billing", "transaction",
    },
}


def _normalize(text: str) -> str:
    """Normalize text for keyword matching."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _score_text(text: str) -> dict[str, int]:
    """Calculate keyword scores for each domain."""
    normalized_text = _normalize(text)
    tokens = normalized_text.split()
    scores = {domain: 0 for domain in DOMAIN_KEYWORDS}

    for domain, keywords in DOMAIN_KEYWORDS.items():
        for keyword in keywords:
            normalized_keyword = _normalize(keyword)

            if " " in normalized_keyword:
                if normalized_keyword in normalized_text:
                    scores[domain] += 2
            elif normalized_keyword in tokens:
                scores[domain] += 1

    return scores


def route(
    question: str,
    history: list[dict] | None = None,
) -> tuple[str, float]:
    """Return the predicted domain and confidence score.

    Conversation history is used when the current question
    does not contain recognizable domain keywords.
    """
    normalized_question = _normalize(question)

    if not normalized_question:
        return "hr", 0.0

    scores = _score_text(normalized_question)
    ranked = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    best_domain, best_score = ranked[0]
    second_score = ranked[1][1]

    if best_score > 0:
        confidence = min(
            0.99,
            0.60
            + 0.10 * best_score
            + 0.10 * (best_score - second_score),
        )
        return best_domain, confidence

    if history:
        for message in reversed(history):
            if message.get("role") != "user":
                continue

            previous_text = message.get("content", "")

            if not isinstance(previous_text, str):
                continue

            previous_scores = _score_text(previous_text)
            previous_domain, previous_score = max(
                previous_scores.items(),
                key=lambda item: item[1],
            )

            if previous_score > 0:
                return previous_domain, 0.65

            break

    return "hr", 0.0

