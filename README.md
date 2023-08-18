# Game Simulation API

This is a REST API service that supports a game simulation. The primary focus is on efficient handling of concurrent requests and optimal utilization of system resources.

## Features Implemented

### 1. Board Initialization

- Endpoint: `/init_board`
- Initializes the game board with a grid 50x50 simulation space.
- Places 10 robots at specified positions.
- Places 50 dinosaurs at specific locations.

### 2. Player Actions

- Endpoint: `/move_robot`
- Allows players to move robots.
- Players can give instructions to a robot using its ID.
- A robot can move up, down, left, or right.
- A robot attack destroys dinosaurs around it (if a dinosaur is in the top, left, right, or bottom cell).
- Players gain one point for killing a dinosaur.

### 3. State

- Endpoint: `/get_state`
- Returns the simulation's current state, including grid size, robot positions, dinosaur locations, and player points.

## How to Run

Open a terminal and navigate to the project directory.

Build the Docker image using the following command:
```shell
docker build -t game-simulation .
```
Once the image is built, you can run a Docker container based on the image:
```shell
docker run -d -p 8000:80 game-simulation
```

## Testing

To run the tests, make sure you have `pytest` installed (`pip install pytest`), and then execute the tests using:

```shell
pytest app/tests/
```
## Challenges and Approach



**Challenges:**

1. **Concurrent Request Handling:** As 10 players can simultaneously control robots in the game, ensuring seamless concurrent request handling is vital to prevent data inconsistencies and conflicts.

2. **Optimal Resource Utilization:** Efficiently utilizing system resources, especially during intensive actions like robot movement and dinosaur destruction, is crucial to maintain high performance.

3. **Modular and Maintainable Design:** Designing a modular and well-structured codebase is essential for code maintainability and future enhancements. Separating components and ensuring clear interactions between them is a challenge.

4. **Error Handling and User-Friendly API:** Providing meaningful error messages and handling unexpected situations gracefully is necessary to improve user experience and prevent system failures.

5. **Asynchronous Implementation:** The asynchronous nature of the game, where players can control robots at their preferred frequency, adds complexity to the implementation to ensure responsiveness and fairness.

6. **Comprehensive Testing:** Writing thorough unit and integration tests is essential to verify the correctness of the implemented features and prevent regressions.

**Approach:**

1. **Concurrent Request Handling:** To handle concurrent requests, I utilized a thread-safe lock mechanism during board initialization to ensure it occurs only once. This prevents race conditions and guarantees a consistent initial game state.

2. **Optimal Resource Utilization:** By using FastAPI's asynchronous capabilities, I enhanced the responsiveness of the API. I carefully designed asynchronous handlers for player actions, such as robot movement and dinosaur destruction, to minimize blocking and maximize resource utilization.

3. **Modular and Maintainable Design:** The project adopts a modular design approach, with separate modules for board initialization, player actions, and state retrieval. This clear separation allows for easy maintenance, debugging, and scalability.

4. **Error Handling and User-Friendly API:** I implemented detailed error handling to provide informative responses to clients, guiding them on how to rectify input errors. Additionally, well-documented API endpoints enhance user-friendliness and facilitate integration.

5. **Asynchronous Implementation:** The project utilizes FastAPI's async features to allow players to control robots at their preferred frequency. Asynchronous handlers ensure responsiveness without blocking other actions, enhancing fairness and interactivity.

6. **Comprehensive Testing:** I developed comprehensive unit tests for each module and integration tests to validate interactions between components. This testing approach ensures that the implemented features work as intended and that changes do not introduce regressions.


