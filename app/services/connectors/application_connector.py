from app.services.connectors.base_connector import BaseConnector

from app.models.execution_result import ExecutionResult
from app.models.remediation_plan import RemediationAction


class ApplicationConnector(BaseConnector):
    """
    Executes application-related actions.

    Currently simulated.

    Can later be replaced with:

    - SSH

    - Docker

    - Kubernetes

    - Azure

    without changing AutomationAgent.
    """

    def execute(
        self,
        action: RemediationAction
    ) -> ExecutionResult:

        return ExecutionResult(

            action_id=action.action_id,

            action=action.action,

            status="SUCCESS",

            execution_mode="SIMULATED",

            message="Application action executed successfully."

        )