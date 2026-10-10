"""LangGraph workflow. Owner: Person 2.

Nodes: load_memory -> route -> retrieve -> agent (tools) -> answer -> save_memory
Enforce MAX_STEPS and MAX_TOOL_CALLS; fall back with explicit uncertainty.
"""
from src.schemas import AgentState


def build_graph():
    """Build and compile the LangGraph workflow."""
    raise NotImplementedError


def run_question(question: str, session_id: str) -> AgentState:
    """Run one question end to end and return the final state (with run_id)."""
    raise NotImplementedError
