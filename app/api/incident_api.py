from fastapi import APIRouter, HTTPException

from app.agents.ai_orchestrator import AIOrchestrator
from app.models.incident import Incident
from app.models.ai_incident_response import AIIncidentResponse


router = APIRouter(
    prefix="/incident",
    tags=["Incident Analysis"]
)


orchestrator = AIOrchestrator()


@router.post(
    "/analyze",
    response_model=AIIncidentResponse,
    summary="Analyze an IT Incident"
)
def analyze_incident(
    incident: Incident
) -> AIIncidentResponse:
    """
    Performs complete AI-powered incident analysis.

    Workflow:

    Incident
        ↓
    Knowledge Retrieval
        ↓
    Diagnosis
        ↓
    Remediation
        ↓
    Final AI Response
    """

    try:

        response = orchestrator.process_incident(
            incident
        )

        return response

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )