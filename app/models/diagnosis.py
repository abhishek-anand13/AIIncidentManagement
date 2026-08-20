from pydantic import BaseModel


class Diagnosis(BaseModel):
    """
    Represents the AI-generated diagnosis for an incident.
    """

    summary: str

    probable_root_cause: str

    reasoning: str

    confidence: str