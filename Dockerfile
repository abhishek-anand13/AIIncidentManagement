# ==========================================
# AI Incident Management - Backend
# ==========================================

FROM python:3.11-slim

# ------------------------------------------
# Python configuration
# ------------------------------------------

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ------------------------------------------
# Working directory
# ------------------------------------------

WORKDIR /app

# ------------------------------------------
# System dependencies
# ------------------------------------------

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ------------------------------------------
# Copy project requirements
# ------------------------------------------

COPY requirements.txt .

# ------------------------------------------
# Upgrade pip
# ------------------------------------------

RUN pip install --no-cache-dir --upgrade pip

# ------------------------------------------
# Install CPU-only PyTorch
# ------------------------------------------

RUN pip install --no-cache-dir \
    torch==2.13.0+cpu \
    --index-url https://download.pytorch.org/whl/cpu

# ------------------------------------------
# Install project dependencies
# ------------------------------------------

RUN pip install --no-cache-dir \
    -r requirements.txt

# ------------------------------------------
# Copy application
# ------------------------------------------

COPY app ./app

# ------------------------------------------
# Copy local incident data
# ------------------------------------------

COPY storage/camunda_incidents.json ./storage/camunda_incidents.json

# ------------------------------------------
# Expose FastAPI
# ------------------------------------------

EXPOSE 8000

# ------------------------------------------
# Start FastAPI
# ------------------------------------------

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]