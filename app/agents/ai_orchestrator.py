from app.agents.knowledge_agent import KnowledgeAgent
from app.agents.diagnostic_agent import DiagnosticAgent
from app.agents.remediation_agent import RemediationAgent
from app.agents.automation_agent import AutomationAgent
from app.agents.verification_agent import VerificationAgent

from app.models.incident import Incident
from app.models.ai_incident_response import AIIncidentResponse


class AIOrchestrator:
    """
    Coordinates the complete AI Incident Management workflow.
    """

    def __init__(self):

        self.knowledge_agent = KnowledgeAgent()

        self.diagnostic_agent = DiagnosticAgent()

        self.remediation_agent = RemediationAgent()

        self.automation_agent = AutomationAgent()

        self.verification_agent = VerificationAgent()

    def process_incident(
        self,
        incident: Incident
    ) -> AIIncidentResponse:

        # ---------------------------------------------
        # Step 1
        # Knowledge Retrieval
        # ---------------------------------------------

        knowledge = self.knowledge_agent.retrieve(
            incident.description
        )

        # ---------------------------------------------
        # Step 2
        # Diagnosis
        # ---------------------------------------------

        diagnosis = self.diagnostic_agent.diagnose(
            incident,
            knowledge
        )

        # ---------------------------------------------
        # Step 3
        # Remediation
        # ---------------------------------------------

        remediation = self.remediation_agent.generate_plan(
            incident,
            knowledge,
            diagnosis
        )

        # ---------------------------------------------
        # Step 4
        # Automation
        # ---------------------------------------------

        automation_results = self.automation_agent.execute(
            remediation
        )

        # ---------------------------------------------
        # Step 5
        # Verification
        # ---------------------------------------------

        verification = self.verification_agent.verify(
            automation_results
        )

        # ---------------------------------------------
        # Step 6
        # Final Response
        # ---------------------------------------------

        return AIIncidentResponse(

            incident=incident,

            knowledge=knowledge,

            diagnosis=diagnosis,

            remediation=remediation,

            automation_results=automation_results,

            verification=verification,

            workflow_status="COMPLETE_WORKFLOW",

            overall_confidence=knowledge.confidence

        )