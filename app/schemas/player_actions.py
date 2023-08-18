from pydantic import BaseModel


class PlayerActionsInputs(BaseModel):
    robot_id: int
    direction: str
