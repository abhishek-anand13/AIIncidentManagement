from app.models.incident import Incident
from app.models.knowledge_context import KnowledgeContext
from app.models.diagnosis import Diagnosis
from app.models.remediation_plan import RemediationPlan

from app.services.llm_service import LLMService


class RemediationAgent:
    """
    Generates an AI remediation plan.

    The generated actions are structured so that they
    can later be executed by the Automation Agent.
    """

    def __init__(self):

        self.llm_service = LLMService()

    def generate_plan(
        self,
        incident: Incident,
        knowledge_context: KnowledgeContext,
        diagnosis: Diagnosis
    ) -> RemediationPlan:

        prompt = self._build_prompt(
            incident,
            knowledge_context,
            diagnosis
        )

        data = self.llm_service.generate(
            prompt=prompt,
            json_mode=True
        )

        return RemediationPlan(**data)

    def _build_prompt(
        self,
        incident: Incident,
        knowledge_context: KnowledgeContext,
        diagnosis: Diagnosis
    ) -> str:

        prompt = f"""
You are a Senior Site Reliability Engineer (SRE).

Your task is to create a production-ready remediation plan.

====================================================
INCIDENT
====================================================

Title:
{incident.title}

Description:
{incident.description}

Priority:
{incident.priority}

====================================================
AI DIAGNOSIS
====================================================

Summary:
{diagnosis.summary}

Probable Root Cause:
{diagnosis.probable_root_cause}

Reasoning:
{diagnosis.reasoning}

Confidence:
{diagnosis.confidence}

====================================================
ENTERPRISE KNOWLEDGE
====================================================

"""

        for chunk in knowledge_context.retrieved_chunks:

            prompt += f"""
----------------------------------------------------

Source:
{chunk.source}

Category:
{chunk.category}

Section:
{chunk.section}

Content:
{chunk.content}

"""

        prompt += """

====================================================
TASK
====================================================

Generate a remediation plan.

IMPORTANT:

Each remediation action must include an action_id.

Use ONLY one of the following action_ids whenever applicable:

restart_application

restart_worker

restart_database

increase_connection_pool

terminate_slow_queries

reduce_traffic

notify_team

create_ticket

manual_investigation

If none fit perfectly, use:

manual_investigation

automation_supported should be:

true
for actions that an automation agent could execute.

false
for actions requiring human judgement.

====================================================
OUTPUT FORMAT
====================================================

Return ONLY valid JSON.

{
    "summary": "...",

    "recommended_actions":[

        {
            "action_id":"restart_application",

            "action":"Restart Application Service",

            "reason":"Refresh database connections",

            "automation_supported":true
        }

    ],

    "verification_steps":[

        {
            "step":"...",

            "expected_result":"..."
        }

    ],

    "escalation_required":false,

    "escalation_reason":"..."
}

Rules:

Return ONLY JSON.

No markdown.

No explanations.

At least 3 recommended_actions.

At least 3 verification_steps.

"""

        return prompt