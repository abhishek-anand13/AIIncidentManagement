from app.models.remediation_plan import RemediationPlan
from app.models.execution_result import ExecutionResult

from app.services.connectors.connector_registry import ConnectorRegistry


class AutomationAgent:
    """
    Executes AI-generated remediation actions.

    The Automation Agent never knows HOW an action
    is executed.

    It delegates execution to the appropriate connector.
    """

    def __init__(self):

        self.registry = ConnectorRegistry()

    def execute(
        self,
        plan: RemediationPlan
    ) -> list[ExecutionResult]:

        results = []

        for action in plan.recommended_actions:

            # Human-only action

            if not action.automation_supported:

                results.append(

                    ExecutionResult(

                        action_id=action.action_id,

                        action=action.action,

                        status="SKIPPED",

                        execution_mode="MANUAL",

                        message="Requires human approval."

                    )

                )

                continue

            connector = self.registry.get_connector(
                action.action_id
            )

            # No connector found

            if connector is None:

                results.append(

                    ExecutionResult(

                        action_id=action.action_id,

                        action=action.action,

                        status="SKIPPED",

                        execution_mode="UNSUPPORTED",

                        message="No connector available."

                    )

                )

                continue

            # Execute

            result = connector.execute(action)

            results.append(result)

        return results