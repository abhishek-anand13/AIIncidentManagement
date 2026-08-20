from app.agents.automation_agent import AutomationAgent
from app.agents.verification_agent import VerificationAgent

from app.models.remediation_plan import (
    RemediationPlan,
    RemediationAction,
    VerificationStep
)


plan = RemediationPlan(

    summary="Database Timeout Remediation",

    recommended_actions=[

        RemediationAction(

            action_id="restart_application",

            action="Restart Application Service",

            reason="Refresh database connections",

            automation_supported=True

        ),

        RemediationAction(

            action_id="increase_connection_pool",

            action="Increase Connection Pool",

            reason="Reduce connection contention",

            automation_supported=True

        ),

        RemediationAction(

            action_id="notify_team",

            action="Notify Operations Team",

            reason="Inform stakeholders",

            automation_supported=True

        ),

        RemediationAction(

            action_id="manual_investigation",

            action="Investigate deployment logs",

            reason="Requires human judgement",

            automation_supported=False

        )

    ],

    verification_steps=[

        VerificationStep(

            step="Verify login",

            expected_result="Users can login"

        )

    ],

    escalation_required=False,

    escalation_reason=""

)

# -----------------------------
# Automation
# -----------------------------

automation_agent = AutomationAgent()

execution_results = automation_agent.execute(plan)

# -----------------------------
# Verification
# -----------------------------

verification_agent = VerificationAgent()

verification = verification_agent.verify(
    execution_results
)

print("=" * 80)
print("VERIFICATION SUMMARY")
print("=" * 80)

print()

print(f"Overall Status     : {verification.overall_status}")

print(f"Successful Actions : {verification.successful_actions}")

print(f"Failed Actions     : {verification.failed_actions}")

print(f"Manual Actions     : {verification.manual_actions}")

print()

print("Recommendation")
print("-" * 80)

print(verification.recommendation)

print()

print("=" * 80)
print("AUTOMATION EXECUTION RESULTS")
print("=" * 80)

for result in execution_results:

    print()

    print(f"Action            : {result.action}")

    print(f"Status            : {result.status}")

    print(f"Execution Mode    : {result.execution_mode}")

    print(f"Message           : {result.message}")