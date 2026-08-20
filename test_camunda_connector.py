from app.integrations.camunda_connector import CamundaConnector


connector = CamundaConnector()

print("=" * 70)
print("PENDING INCIDENTS")
print("=" * 70)

incidents = connector.get_pending_incidents()

for incident in incidents:

    print()

    print(f"ID          : {incident['incident_id']}")
    print(f"Title       : {incident['title']}")
    print(f"Priority    : {incident['priority']}")
    print(f"Status      : {incident['status']}")