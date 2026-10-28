
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "ok"
    assert data["service"] == "deployx"
    assert "timestamp" in data


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to DeployX"


def test_readiness_endpoint():
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ready",
        "service": "deployx",
    }
