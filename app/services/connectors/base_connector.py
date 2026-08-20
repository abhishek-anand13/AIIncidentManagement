from abc import ABC
from abc import abstractmethod

from app.models.execution_result import ExecutionResult
from app.models.remediation_plan import RemediationAction


class BaseConnector(ABC):
    """
    Base class for every enterprise connector.
    """

    @abstractmethod
    def execute(
        self,
        action: RemediationAction
    ) -> ExecutionResult:
        pass