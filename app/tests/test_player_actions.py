from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_move_robot_successful():
    response = client.post("/init_board")
    assert response.status_code == 200

    response = client.post(f"/move_robot/", json={"robot_id": 0, "direction": "right"})
    assert response.status_code == 200
    assert response.json() == {"message": "Robot moved successfully"}


def test_move_robot_invalid_direction():
    response = client.post("/init_board")
    assert response.status_code == 200

    response = client.post("/move_robot", json={"robot_id": 0, "direction": "invalid"})
    assert response.status_code == 400


def test_move_robot_robot_not_found():
    response = client.post("/init_board")
    assert response.status_code == 200

    response = client.post("/move_robot", json={"robot_id": 999, "direction": "right"})
    assert response.status_code == 404
