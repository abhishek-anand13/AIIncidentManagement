import json
from pathlib import Path


class CamundaConnector:
    """
    Simulates communication with Camunda.

    Today:
        Reads and updates incidents stored in JSON.

    Future:
        Replace these methods with real Camunda REST API calls
        without changing the rest of the application.
    """

    def __init__(self):

        self.storage = (
            Path(__file__)
            .resolve()
            .parent.parent.parent
            / "storage"
            / "camunda_incidents.json"
        )

    # --------------------------------------------------
    # Internal Helpers
    # --------------------------------------------------

    def _load(self):

        with open(self.storage, "r", encoding="utf-8") as f:

            return json.load(f)

    def _save(self, incidents):

        with open(self.storage, "w", encoding="utf-8") as f:

            json.dump(
                incidents,
                f,
                indent=4
            )

    # --------------------------------------------------
    # Public Methods
    # --------------------------------------------------

    def get_pending_incidents(self):

        incidents = self._load()

        return [

            incident

            for incident in incidents

            if incident["status"] == "WAITING_FOR_AI"

        ]

    def get_incident(self, incident_id):

        incidents = self._load()

        for incident in incidents:

            if incident["incident_id"] == incident_id:

                return incident

        return None

    def mark_in_progress(self, incident_id):

        incidents = self._load()

        for incident in incidents:

            if incident["incident_id"] == incident_id:

                incident["status"] = "AI_IN_PROGRESS"

        self._save(incidents)

    def mark_completed(self, incident_id):

        incidents = self._load()

        for incident in incidents:

            if incident["incident_id"] == incident_id:

                incident["status"] = "AI_COMPLETED"

        self._save(incidents)

    def save_ai_response(
        self,
        incident_id,
        response
    ):

        incidents = self._load()

        for incident in incidents:

            if incident["incident_id"] == incident_id:

                incident["ai_response"] = response

        self._save(incidents)
        