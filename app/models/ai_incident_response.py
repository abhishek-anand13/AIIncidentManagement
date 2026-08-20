from pydantic import BaseModel

from app.models.incident import Incident
from app.models.knowledge_context import KnowledgeContext
from app.models.diagnosis import Diagnosis
from app.models.remediation_plan import RemediationPlan
from app.models.execution_result import ExecutionResult
from app.models.verification_result import VerificationResult


class AIIncidentResponse(BaseModel):
    """
    Final response returned by the AI Orchestrator.
    """

    incident: Incident

    knowledge: KnowledgeContext

    diagnosis: Diagnosis | None = None

    remediation: RemediationPlan | None = None

    automation_results: list[ExecutionResult] | None = None

    verification: VerificationResult | None = None

    workflow_status: str

    overall_confidence: str