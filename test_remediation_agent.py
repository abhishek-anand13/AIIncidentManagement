from app.models.incident import Incident

from app.agents.knowledge_agent import KnowledgeAgent
from app.agents.diagnostic_agent import DiagnosticAgent
from app.agents.remediation_agent import RemediationAgent


incident = Incident(
    title="Database Timeout",
    description="Users cannot login after deployment because of database connection timeout.",
    priority="High"
)

knowledge_agent = KnowledgeAgent()

knowledge = knowledge_agent.retrieve(
    incident.description
)

diagnostic_agent = DiagnosticAgent()

diagnosis = diagnostic_agent.diagnose(
    incident,
    knowledge
)

remediation_agent = RemediationAgent()

plan = remediation_agent.generate_plan(
    incident,
    knowledge,
    diagnosis
)

print("=" * 70)
print("AI REMEDIATION PLAN")
print("=" * 70)

print("\nSummary:")
print(plan.summary)

print("\nRecommended Actions")

print("-" * 70)

for i, action in enumerate(plan.recommended_actions, start=1):

    print(f"\nAction {i}")

    print(f"Action : {action.action}")

    print(f"Reason : {action.reason}")

print("\nVerification Steps")

print("-" * 70)

for i, step in enumerate(plan.verification_steps, start=1):

    print(f"\nStep {i}")

    print(f"Step            : {step.step}")

    print(f"Expected Result : {step.expected_result}")

print("\nEscalation Required")

print("-" * 70)

print(plan.escalation_required)

print("\nEscalation Reason")

print("-" * 70)

print(plan.escalation_reason)

print("\nComplete Object")

print("-" * 70)

try:

    print(plan.model_dump())

except AttributeError:

    print(plan.dict())