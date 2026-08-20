from fastapi import FastAPI
from app.api.incident_api import router as incident_router
from app.api.camunda_api import router as camunda_router


app = FastAPI(

    title="AI Incident Management System",

    description="""
An AI-powered Incident Management System that performs:

- Knowledge Retrieval (RAG)
- AI Root Cause Analysis
- AI Remediation Planning
- Confidence Evaluation
- Multi-Agent Orchestration
""",

    version="1.0.0"

)

app.include_router(incident_router)
app.include_router(camunda_router)


@app.get("/")
def root():

    return {

        "message": "AI Incident Management System",

        "status": "Running"

    }