from app.models.incident import Incident
from app.models.knowledge_context import KnowledgeContext
from app.models.diagnosis import Diagnosis

from app.services.llm_service import LLMService


class DiagnosticAgent:
    """
    Uses the LLM to analyze production incidents
    using enterprise knowledge retrieved by the
    Knowledge Agent.
    """

    def __init__(self):

        self.llm_service = LLMService()

    def diagnose(
        self,
        incident: Incident,
        knowledge_context: KnowledgeContext
    ) -> Diagnosis:
        """
        Analyze the incident using the LLM.
        """

        prompt = self._build_prompt(
            incident,
            knowledge_context
        )

        # Ask Ollama to return JSON
        data = self.llm_service.generate(
            prompt=prompt,
            json_mode=True
        )

        # Convert JSON into a Pydantic model
        return Diagnosis(**data)

    def _build_prompt(
        self,
        incident: Incident,
        knowledge_context: KnowledgeContext
    ) -> str:
        """
        Build a structured prompt for the LLM.
        """

        prompt = f"""
You are an experienced Site Reliability Engineer (SRE).

Your task is to analyze a production incident using ONLY the incident details and the enterprise knowledge provided below.

========================
INCIDENT DETAILS
========================

Title:
{incident.title}

Description:
{incident.description}

Priority:
{incident.priority}

========================
ENTERPRISE KNOWLEDGE
========================

"""

        for chunk in knowledge_context.retrieved_chunks:

            prompt += f"""
----------------------------------------
Source   : {chunk.source}
Category : {chunk.category}
Section  : {chunk.section}

Content:
{chunk.content}

"""

        prompt += """

========================
YOUR TASK
========================

Analyze the production incident.

Determine:

1. Incident Summary
2. Most Probable Root Cause
3. Reasoning
4. Confidence

========================
OUTPUT FORMAT
========================

Return ONLY a valid JSON object.

Schema:

{
    "summary": "string",
    "probable_root_cause": "string",
    "reasoning": "string",
    "confidence": "HIGH | MEDIUM | LOW"
}

Rules:

- Return ONLY the JSON object.
- Do NOT use markdown.
- Do NOT wrap the JSON in triple backticks.
- Do NOT include explanations.
- Confidence must be exactly one of:
  HIGH
  MEDIUM
  LOW

"""

        return prompt