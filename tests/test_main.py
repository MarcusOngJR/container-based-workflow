

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add() -> None:
    payload = {"a": 1, "b": 2}
    response = client.post("/add", json=payload)
    assert response.status_code == 200
    assert response.json()["result"] == 3


def test_subtract() -> None:
    payload = {"a": 5, "b": 3}
    response = client.post("/subtract", json=payload)
    assert response.status_code == 200
    assert response.json()["result"] == 2


def test_multiply() -> None:
    payload = {"a": 2, "b": 4}
    response = client.post("/multiply", json=payload)
    assert response.status_code == 200
    assert response.json()["result"] == 8


def test_divide() -> None:
    payload = {"a": 10, "b": 2}
    response = client.post("/divide", json=payload)
    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_divide_by_zero() -> None:
    payload = {"a": 10, "b": 0}
    response = client.post("/divide", json=payload)
    assert response.status_code == 400
    data = response.json()
    assert data["detail"] == "Cannot divide by zero."
