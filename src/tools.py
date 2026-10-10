"""Three typed tools. Owner: Person 3.

Each tool = Pydantic input schema + typed function. Bad input must be caught
and returned to the agent as feedback (one retry).
"""
from pydantic import BaseModel


class PolicyLookupInput(BaseModel):
    """Input for looking up a policy by ID or topic."""

    query: str


class ReimbursementInput(BaseModel):
    """Input for the reimbursement calculator."""

    items: list[dict]


class ListLeaveTypesInput(BaseModel):
    """Input for listing leave types (no arguments needed)."""


def policy_lookup(args: PolicyLookupInput) -> str:
    """Look up a policy."""
    raise NotImplementedError


def reimbursement_calculator(args: ReimbursementInput) -> str:
    """Calculate a reimbursement total."""
    raise NotImplementedError


def list_leave_types(args: ListLeaveTypesInput) -> str:
    """List available leave types."""
    raise NotImplementedError


TOOLS = {
    "policy_lookup": (PolicyLookupInput, policy_lookup),
    "reimbursement_calculator": (ReimbursementInput, reimbursement_calculator),
    "list_leave_types": (ListLeaveTypesInput, list_leave_types),
}
