import uvicorn
from fastapi import FastAPI

from app.api import board, player_actions, state

app = FastAPI()

app.include_router(board.router)
app.include_router(player_actions.router)
app.include_router(state.router)
if __name__ == '__main__':
    uvicorn.run('__main__:app', host="0.0.0.0", port=4000, reload=True)
