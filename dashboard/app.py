import requests
import streamlit as st
import pandas as pd

API_URL = "http://127.0.0.1:8000"

# ----------------------------------------------------
# PAGE
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Operations Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Operations Copilot")
st.caption("Enterprise AI Incident Management System")

st.divider()

# ----------------------------------------------------
# LOAD INCIDENTS
# ----------------------------------------------------

try:

    response = requests.get(
        f"{API_URL}/camunda/incidents"
    )

    incidents = response.json()

except Exception:

    st.error("Cannot connect to FastAPI.")

    st.stop()

# ----------------------------------------------------
# INCIDENT QUEUE
# ----------------------------------------------------

st.header("📋 Pending Camunda Incidents")

if not incidents:

    st.success("No pending incidents.")

    st.stop()

selected_response = None

for incident in incidents:

    col1, col2, col3, col4, col5 = st.columns(
        [1,3,1,2,1]
    )

    col1.write(
        incident.get("incident_id", incident.get("id"))
    )

    col2.write(
        incident["title"]
    )

    col3.write(
        incident["priority"]
    )

    col4.write(
        incident["status"]
    )

    if col5.button(
        "Analyze",
        key=incident.get("incident_id", incident.get("id"))
    ):

        with st.spinner(
            "Analyzing Incident..."
        ):

            analyze = requests.post(

                f"{API_URL}/camunda/analyze/{incident.get('incident_id', incident.get('id'))}"

            )

        if analyze.status_code == 200:

            selected_response = analyze.json()

        else:

            st.error(analyze.text)

st.divider()

# ----------------------------------------------------
# WAIT
# ----------------------------------------------------

if selected_response is None:

    st.info(
        "Click Analyze to start AI analysis."
    )

    st.stop()

data = selected_response

# ----------------------------------------------------
# WORKFLOW
# ----------------------------------------------------

# ----------------------------------------------------
# WORKFLOW OVERVIEW
# ----------------------------------------------------

st.header("📊 Workflow Overview")

c1, c2, c3 = st.columns(3)

knowledge_confidence = data["knowledge"]["confidence"]
workflow_status = data["workflow_status"].replace("_", " ").title()
overall_confidence = data["overall_confidence"]

c1.metric(
    "Knowledge Confidence",
    knowledge_confidence
)

c2.metric(
    "Workflow Status",
    workflow_status
)

c3.metric(
    "Overall Confidence",
    overall_confidence
)

st.divider()

# ----------------------------------------------------
# INCIDENT
# ----------------------------------------------------

st.header("🚨 Incident")

st.write(
    f"### {data['incident']['title']}"
)

st.write(
    data["incident"]["description"]
)

st.write(
    f"**Priority:** {data['incident']['priority']}"
)

st.divider()

# ----------------------------------------------------
# KNOWLEDGE RETRIEVAL
# ----------------------------------------------------

knowledge = data["knowledge"]

st.header("📚 Knowledge Retrieval")

if knowledge["found"]:

    st.success(
        f"Retrieved {len(knowledge['retrieved_chunks'])} relevant knowledge documents."
    )

    for chunk in knowledge["retrieved_chunks"]:

        with st.expander(
            f"{chunk['source']} | Similarity Distance : {round(chunk['distance'], 4)}"
        ):

            st.write(f"**Category:** {chunk['category']}")

            st.write(f"**Section:** {chunk['section']}")

            st.info(chunk["content"])

else:

    st.warning("No relevant enterprise knowledge was retrieved.")

st.divider()

# ----------------------------------------------------
# DIAGNOSIS
# ----------------------------------------------------

diagnosis = data["diagnosis"]

st.header("🩺 Diagnosis")

st.success(
    diagnosis["summary"]
)

st.error(
    diagnosis["probable_root_cause"]
)

st.write(
    diagnosis["reasoning"]
)

st.write(
    f"Confidence : {diagnosis['confidence']}"
)

st.divider()

# ----------------------------------------------------
# REMEDIATION PLAN
# ----------------------------------------------------

remediation = data["remediation"]

st.header("🛠️ Remediation Plan")

st.success(
    remediation["summary"]
)

st.subheader("Recommended Actions")

actions = []

for action in remediation["recommended_actions"]:

    actions.append({

        "Action": action["action"],

        "Reason": action["reason"],

        "Automation": "✅ YES" if action["automation_supported"] else "❌ NO"

    })

st.dataframe(
    pd.DataFrame(actions),
    use_container_width=True,
    hide_index=True
)

st.subheader("Verification Steps")

verification_steps = []

for step in remediation["verification_steps"]:

    verification_steps.append({

        "Step": step["step"],

        "Expected Result": step["expected_result"]

    })

st.dataframe(
    pd.DataFrame(verification_steps),
    use_container_width=True,
    hide_index=True
)

if remediation["escalation_required"]:

    st.error(
        f"Escalation Required: {remediation['escalation_reason']}"
    )

st.divider()

# ----------------------------------------------------
# AUTOMATION RESULTS
# ----------------------------------------------------

automation = data["automation_results"]

st.header("⚙️ Automation Results")

automation_rows = []

for result in automation:

    if result["status"] == "SUCCESS":

        status = "🟢 SUCCESS"

    elif result["status"] == "FAILED":

        status = "🔴 FAILED"

    elif result["status"] == "SKIPPED":

        status = "🟡 SKIPPED"

    else:

        status = result["status"]

    automation_rows.append({

        "Action": result["action"],

        "Status": status,

        "Execution": result["execution_mode"],

        "Message": result["message"]

    })

st.dataframe(

    pd.DataFrame(automation_rows),

    use_container_width=True,

    hide_index=True

)

st.divider()
# ----------------------------------------------------
# VERIFICATION
# ----------------------------------------------------

verification = data["verification"]

st.header("✅ Verification")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Overall Status",
    verification["overall_status"].replace("_", " ")
)

col2.metric(
    "Successful",
    verification["successful_actions"]
)

col3.metric(
    "Failed",
    verification["failed_actions"]
)

col4.metric(
    "Manual",
    verification["manual_actions"]
)

st.info(
    verification["recommendation"]
)

st.divider()
# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.caption(
    "AI Operations Copilot • Multi-Agent AI Incident Management System"
)