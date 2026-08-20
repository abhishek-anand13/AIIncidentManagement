from app.agents.ai_orchestrator import AIOrchestrator

from app.models.incident import Incident


incident = Incident(

    title="Database Timeout",

    description="Users cannot login after deployment because of database connection timeout.",

    priority="High"

)


orchestrator = AIOrchestrator()

response = orchestrator.process_incident(
    incident
)

print("=" * 80)
print("AI INCIDENT MANAGEMENT SYSTEM")
print("=" * 80)

# ============================================================
# INCIDENT
# ============================================================

print("\nINCIDENT")
print("-" * 80)

print(f"Title       : {response.incident.title}")
print(f"Description : {response.incident.description}")
print(f"Priority    : {response.incident.priority}")

# ============================================================
# KNOWLEDGE
# ============================================================

print("\nKNOWLEDGE RETRIEVAL")
print("-" * 80)

print(f"Confidence : {response.knowledge.confidence}")
print(f"Chunks      : {len(response.knowledge.retrieved_chunks)}")

# ============================================================
# DIAGNOSIS
# ============================================================

if response.diagnosis:

    print("\nDIAGNOSIS")
    print("-" * 80)

    print(f"Summary : {response.diagnosis.summary}")

    print("\nRoot Cause:")
    print(response.diagnosis.probable_root_cause)

    print("\nReasoning:")
    print(response.diagnosis.reasoning)

    print("\nConfidence:")
    print(response.diagnosis.confidence)

# ============================================================
# REMEDIATION
# ============================================================

if response.remediation:

    print("\nREMEDIATION PLAN")
    print("-" * 80)

    print("\nSummary:")
    print(response.remediation.summary)

    print("\nRecommended Actions:")

    for i, action in enumerate(
        response.remediation.recommended_actions,
        start=1
    ):

        print(f"\n{i}. {action.action}")

        print(f"   Action ID             : {action.action_id}")

        print(f"   Reason                : {action.reason}")

        print(f"   Automation Supported  : {action.automation_supported}")

    print("\nVerification Steps:")

    for i, step in enumerate(
        response.remediation.verification_steps,
        start=1
    ):

        print(f"\n{i}. {step.step}")

        print(f"   Expected Result : {step.expected_result}")

    print("\nEscalation Required:")
    print(response.remediation.escalation_required)

    print("\nEscalation Reason:")
    print(response.remediation.escalation_reason)

# ============================================================
# AUTOMATION
# ============================================================

if response.automation_results:

    print("\nAUTOMATION RESULTS")
    print("-" * 80)

    for i, result in enumerate(
        response.automation_results,
        start=1
    ):

        print(f"\nAction {i}")

        print(f"Action ID      : {result.action_id}")

        print(f"Action         : {result.action}")

        print(f"Status         : {result.status}")

        print(f"Execution Mode : {result.execution_mode}")

        print(f"Message        : {result.message}")

# ============================================================
# VERIFICATION
# ============================================================

if response.verification:

    print("\nVERIFICATION")
    print("-" * 80)

    print(f"Overall Status     : {response.verification.overall_status}")

    print(f"Successful Actions : {response.verification.successful_actions}")

    print(f"Failed Actions     : {response.verification.failed_actions}")

    print(f"Manual Actions     : {response.verification.manual_actions}")

    print("\nRecommendation:")

    print(response.verification.recommendation)

# ============================================================
# WORKFLOW
# ============================================================

print("\nWORKFLOW")
print("-" * 80)

print(f"Workflow Status    : {response.workflow_status}")

print(f"Overall Confidence : {response.overall_confidence}")

print("\n" + "=" * 80)
print("END OF ANALYSIS")
print("=" * 80)