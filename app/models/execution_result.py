from pydantic import BaseModel


class ExecutionResult(BaseModel):
    """
    Represents the result of executing
    a remediation action.
    """

    action_id: str

    action: str

    status: str

    execution_mode: str

    message: str