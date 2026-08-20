from pydantic import BaseModel


class RemediationAction(BaseModel):
    """
    Represents a single remediation action.

    These actions are intentionally structured so they can
    later be executed by the Automation Agent.
    """

    action_id: str

    action: str

    reason: str

    automation_supported: bool


class VerificationStep(BaseModel):
    """
    Represents a verification step.
    """

    step: str

    expected_result: str


class RemediationPlan(BaseModel):
    """
    Complete AI-generated remediation plan.
    """

    summary: str

    recommended_actions: list[RemediationAction]

    verification_steps: list[VerificationStep]

    escalation_required: bool

    escalation_reason: str