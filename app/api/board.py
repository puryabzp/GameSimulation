from fastapi import APIRouter
import random
import threading

router = APIRouter()

GRID_SIZE = (50, 50)
NUM_ROBOTS = 10
NUM_DINOSAURS = 50

board = {
    "grid_size": GRID_SIZE,
    "robots": {},
    "dinosaurs": [],
    "player_points": {}
}

init_lock = threading.Lock()
init_done = False


@router.post("/init_board")
async def initialize_board():
    """
    Initialize the game board with robots and dinosaurs.

    returns:
        dict: A message indicating the board initialization status.
    """

    global init_done
    with init_lock:
        if init_done:
            return {"message": "Board already initialized"}

        for i in range(NUM_ROBOTS):
            x, y = random.randint(0, GRID_SIZE[0] - 1), random.randint(0, GRID_SIZE[1] - 1)
            board["robots"][i] = {"x": x, "y": y}

        for _ in range(NUM_DINOSAURS):
            x, y = random.randint(0, GRID_SIZE[0] - 1), random.randint(0, GRID_SIZE[1] - 1)
            board["dinosaurs"].append({"x": x, "y": y})

        init_done = True
        return {"message": "Board initialized"}
