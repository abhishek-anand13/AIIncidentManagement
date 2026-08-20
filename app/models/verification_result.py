from pydantic import BaseModel


class VerificationResult(BaseModel):
    """
    Represents the outcome of verifying
    the automation execution.
    """

    overall_status: str

    successful_actions: int

    failed_actions: int

    manual_actions: int

    recommendation: str