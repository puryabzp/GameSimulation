from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_init_board():
    response = client.post("/init_board")
    assert response.status_code == 200
    assert response.json() == {"message": "Board initialized"}


def test_init_board_already_initialized():
    response = client.post("/init_board")
    assert response.status_code == 200
    assert response.json() == {"message": "Board already initialized"}
