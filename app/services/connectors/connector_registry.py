from app.services.connectors.application_connector import ApplicationConnector
from app.services.connectors.database_connector import DatabaseConnector
from app.services.connectors.notification_connector import NotificationConnector


class ConnectorRegistry:
    """
    Maps action_ids to the connector responsible
    for executing that action.
    """

    def __init__(self):

        self.application = ApplicationConnector()

        self.database = DatabaseConnector()

        self.notification = NotificationConnector()

        self.mapping = {

            # Application

            "restart_application": self.application,

            "restart_worker": self.application,

            # Database

            "restart_database": self.database,

            "increase_connection_pool": self.database,

            "terminate_slow_queries": self.database,

            "reduce_traffic": self.database,

            # Notifications

            "notify_team": self.notification,

            "create_ticket": self.notification,

            # Unknown

            "manual_investigation": None

        }

    def get_connector(self, action_id: str):

        return self.mapping.get(action_id)