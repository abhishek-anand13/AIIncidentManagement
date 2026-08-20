from pydantic import BaseModel, Field


class Incident(BaseModel):
    """
    Represents an incident submitted by the user.
    """

    title: str = Field(..., example="Database Connection Timeout")

    description: str = Field(
        ...,
        example="Users cannot access the application after deployment."
    )

    priority: str = Field(
        ...,
        example="High"
    )