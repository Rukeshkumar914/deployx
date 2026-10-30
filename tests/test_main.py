from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["service"] == "deployx"
    assert "timestamp" in response.json()
    assert response.json()["version"] == "1.0.0"


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to DeployX"
    assert response.json()["service"] == "deployx"
    assert response.json()["version"] == "1.0.0"


def test_readiness_endpoint():
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ready",
        "service": "deployx",
        "version": "1.0.0",
    }
