from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Laptop", "price": 1500.99})
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1