from fastapi import APIRouter
from app.api.board import board

router = APIRouter()


@router.get("/get_state")
async def get_simulation_state():
    """
    Get the current state of the game simulation.

    returns: dict: The current state of the game including grid size, robot positions, dinosaur
    positions, and player points.
    """

    state = {
        "grid_size": board["grid_size"],
        "robots": board["robots"],
        "dinosaurs": board["dinosaurs"],
        "player_points": board["player_points"]
    }
    return state
