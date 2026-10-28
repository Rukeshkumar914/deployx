
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="DeployX API",
    description="Health check API for automated deployment",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to DeployX",
        "health": "/health",
        "readiness": "/ready",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "deployx",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/ready")
def readiness_check():
    return {
        "status": "ready",
        "service": "deployx",
    }
