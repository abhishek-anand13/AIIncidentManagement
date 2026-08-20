from app.models.execution_result import ExecutionResult
from app.models.verification_result import VerificationResult


class VerificationAgent:
    """
    Verifies whether the automation phase
    completed successfully.

    This agent intentionally uses deterministic
    business rules instead of an LLM.

    In a real enterprise system this agent could
    later query Azure Monitor, Prometheus,
    Grafana, Elasticsearch, etc.
    """

    def verify(
        self,
        execution_results: list[ExecutionResult]
    ) -> VerificationResult:

        successful_actions = 0
        failed_actions = 0
        manual_actions = 0

        for result in execution_results:

            if result.status == "SUCCESS":

                successful_actions += 1

            elif result.execution_mode == "MANUAL":

                manual_actions += 1

            else:

                failed_actions += 1

        # --------------------------------------------------
        # Determine Overall Status
        # --------------------------------------------------

        if failed_actions > 0:

            overall_status = "FAILED"

            recommendation = (
                "Automation encountered failures. "
                "Escalate the incident for investigation."
            )

        elif manual_actions > 0:

            overall_status = "PARTIALLY_VERIFIED"

            recommendation = (
                "Automation completed successfully. "
                "Complete the remaining manual actions "
                "before closing the incident."
            )

        else:

            overall_status = "PASSED"

            recommendation = (
                "All automated actions completed successfully. "
                "The incident is ready for closure."
            )

        return VerificationResult(

            overall_status=overall_status,

            successful_actions=successful_actions,

            failed_actions=failed_actions,

            manual_actions=manual_actions,

            recommendation=recommendation

        )