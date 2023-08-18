from fastapi import APIRouter, HTTPException

from app.api.board import board
from app.schemas import PlayerActionsInputs

router = APIRouter()

DIRECTIONS = {"up", "down", "left", "right"}


@router.post("/move_robot/")
async def move_robot(request_in: PlayerActionsInputs):
    """
        Move a robot on the game board.

        :params:
            robot_id (int): The ID of the robot to be moved.
            direction (str): The direction in which the robot should move.

        returns:
            dict: A message indicating the success of the robot movement.
        """

    robot_id = request_in.robot_id
    direction = request_in.direction
    if direction not in DIRECTIONS:
        raise HTTPException(status_code=400, detail="Invalid direction")

    robot = board["robots"].get(robot_id)
    if not robot:
        raise HTTPException(status_code=404, detail="Robot not found")

    x, y = robot["x"], robot["y"]

    if direction == "up":
        x -= 1
    elif direction == "down":
        x += 1
    elif direction == "left":
        y -= 1
    elif direction == "right":
        y += 1

    if is_valid_move(x, y):
        robot["x"], robot["y"] = x, y
        destroy_dinosaurs_around(robot_id, x, y)
    else:
        raise HTTPException(status_code=400, detail="Invalid move")

    return {"message": "Robot moved successfully"}


def is_valid_move(x, y):
    return 0 <= x < board["grid_size"][0] and 0 <= y < board["grid_size"][1]


def destroy_dinosaurs_around(robot_id, x, y):
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if {"x": new_x, "y": new_y} in board["dinosaurs"]:
            board["dinosaurs"].remove({"x": new_x, "y": new_y})
            increase_player_points(robot_id)


def increase_player_points(robot_id):
    player_id = f"player_{robot_id}"
    board["player_points"][player_id] = board["player_points"].get(player_id, 0) + 1
