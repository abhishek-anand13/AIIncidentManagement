from app.services.connectors.base_connector import BaseConnector

from app.models.execution_result import ExecutionResult
from app.models.remediation_plan import RemediationAction


class NotificationConnector(BaseConnector):

    def execute(
        self,
        action: RemediationAction
    ) -> ExecutionResult:

        return ExecutionResult(

            action_id=action.action_id,

            action=action.action,

            status="SUCCESS",

            execution_mode="SIMULATED",

            message="Notification sent successfully."

        )