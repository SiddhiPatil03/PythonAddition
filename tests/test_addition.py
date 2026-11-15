
from fastapi.testclient import TestClient
from app.main import app
from app.addition import add_numbers

client = TestClient(app)


def test_addition():
    assert add_numbers(10, 20) == 30


def test_addition_negative():
    assert add_numbers(-5, 10) == 5


def test_addition_api():
    response = client.get("/add?a=10&b=20")

    assert response.status_code == 200
    assert response.json()["addition"] == 30


def test_home_api():
    response = client.get("/")

    assert response.status_code == 200
