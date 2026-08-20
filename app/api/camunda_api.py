from fastapi import APIRouter, HTTPException

from app.integrations.camunda_connector import CamundaConnector
from app.agents.ai_orchestrator import AIOrchestrator
from app.models.incident import Incident

router = APIRouter(
    prefix="/camunda",
    tags=["Camunda Integration"]
)

connector = CamundaConnector()

orchestrator = AIOrchestrator()


@router.get("/incidents")
def get_pending_incidents():
    """
    Returns all incidents waiting for AI analysis.
    """

    return connector.get_pending_incidents()


@router.post("/analyze/{incident_id}")
def analyze_camunda_incident(
    incident_id: str
):
    """
    Simulates Camunda sending an incident
    to the AI Operations Copilot.
    """

    incident = connector.get_incident(
        incident_id
    )

    if incident is None:

        raise HTTPException(
            status_code=404,
            detail="Incident not found."
        )

    connector.mark_in_progress(
        incident_id
    )

    ai_incident = Incident(

        title=incident["title"],

        description=incident["description"],

        priority=incident["priority"]

    )

    response = orchestrator.process_incident(
        ai_incident
    )

    connector.save_ai_response(
        incident_id,
        response.model_dump()
    )

    connector.mark_completed(
        incident_id
    )

    return response