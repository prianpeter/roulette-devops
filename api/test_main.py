from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}

def test_predict():
    payload = {"history": [1, 3, 5]}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "suggestion" in data
    assert "last_number_received" in data
    assert data["last_number_received"] == 5
