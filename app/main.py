from fastapi import FastAPI
from datetime import datetime, timezone

from app.config import SERVICE_NAME, APP_VERSION

app = FastAPI(
    title="DeployX API",
    description="Health check API for automated deployment",
    version=APP_VERSION,
)


@app.get("/")
def root():
    return {
        "message": "Welcome to DeployX",
        "service": SERVICE_NAME,
        "version": APP_VERSION,
        "health": "/health",
        "readiness": "/ready",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": SERVICE_NAME,
        "version": APP_VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/ready")
def readiness_check():
    return {
        "status": "ready",
        "service": SERVICE_NAME,
        "version": APP_VERSION,
    }
