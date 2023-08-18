from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_state_after_init():
    response = client.post("/init_board")
    assert response.status_code == 200

    response = client.get("/get_state")
    assert response.status_code == 200
    state = response.json()
    assert state["grid_size"] == [50, 50]
    assert len(state["robots"]) == 10
    assert len(state["dinosaurs"]) == 50
    assert state["player_points"] == {}
