from app.agents.knowledge_agent import KnowledgeAgent
from app.agents.diagnostic_agent import DiagnosticAgent

from app.models.incident import Incident


# --------------------------------------------------------------------
# Create a sample incident
# --------------------------------------------------------------------
incident = Incident(
    title="Database Timeout",
    description="Users cannot login after deployment because of database connection timeout.",
    priority="High"
)


# --------------------------------------------------------------------
# Retrieve enterprise knowledge
# --------------------------------------------------------------------
knowledge_agent = KnowledgeAgent()

knowledge = knowledge_agent.retrieve(
    incident.description
)


# --------------------------------------------------------------------
# Diagnose the incident using the LLM
# --------------------------------------------------------------------
diagnostic_agent = DiagnosticAgent()

diagnosis = diagnostic_agent.diagnose(
    incident,
    knowledge
)


# --------------------------------------------------------------------
# Print Diagnosis
# --------------------------------------------------------------------
print("=" * 70)
print("AI DIAGNOSIS")
print("=" * 70)

print(f"\nSummary:\n{diagnosis.summary}")

print(f"\nProbable Root Cause:\n{diagnosis.probable_root_cause}")

print(f"\nReasoning:\n{diagnosis.reasoning}")

print(f"\nConfidence:\n{diagnosis.confidence}")

print("\n" + "=" * 70)

# --------------------------------------------------------------------
# Debug View (Complete Object)
# --------------------------------------------------------------------
print("\nComplete Diagnosis Object:\n")

try:
    # Pydantic v2
    print(diagnosis.model_dump())

except AttributeError:
    # Pydantic v1
    print(diagnosis.model_dump())