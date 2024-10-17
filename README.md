# Game of Life Simulation

This project implements Conway's Game of Life using Python and `pygame`. It allows users to create, modify, and simulate cellular automata based on simple rules, leading to complex behaviors over time.

## Features

- **Interactive Grid**: Users can toggle cells to create initial patterns.
- **Game Controls**: Start, pause, and reset the simulation.
- **Random Grid Generation**: Populate the grid with a random distribution of live cells.
- **Color Customization**: Change the color of the live cells.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/game-of-life.git
   cd game-of-life
   ```

2. **Install Dependencies**:
   This project requires Python 3.x and the `pygame` and `numpy` libraries.
   You can install the required libraries using pip:
   ```bash
   pip install pygame numpy
   ```

## How to Run

1. After installing the dependencies, run the `main.py` file:
   ```bash
   python main.py
   ```

## Controls

- **Left Click**: Toggle the state of a cell (alive or dead).
- **`SPACE`**: Pause or resume the simulation.
- **`R`**: Generate a random grid.
- **`ESC`**: Quit the game.
- **Color Customization**:
  - **`W`**: Set live cells to white.
  - **`1`**: Set live cells to red.
  - **`2`**: Set live cells to green.
  - **`3`**: Set live cells to blue.
  - **`4`**: Set live cells to pink.
  - **`5`**: Set live cells to yellow.
  - **`6`**: Set live cells to cyan.
  - **`7`**: Set live cells to maroon.

## Game Rules

Conway's Game of Life is a zero-player game where the evolution of cells on a grid follows these rules:

1. **Any live cell with fewer than two live neighbors dies** (underpopulation).
2. **Any live cell with two or three live neighbors lives on to the next generation**.
3. **Any live cell with more than three live neighbors dies** (overpopulation).
4. **Any dead cell with exactly three live neighbors becomes a live cell** (reproduction).

## Code Overview

- **Grid Initialization**:
  A 2D numpy array is used to represent the grid, where `1` represents a live cell and `0` represents a dead cell.
  ```python
  grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)
  ```

- **Drawing the Grid**:
  The grid is drawn based on the cell states. Live cells are drawn in the selected color, while dead cells are black.
  ```python
  def draw_grid(window, grid, color):
      ...
  ```

- **Updating the Grid**:
  The grid is updated based on the rules of the Game of Life.
  ```python
  def update_grid(grid):
      ...
  ```

- **User Input Handling**:
  The simulation handles user input for toggling cells and controlling the simulation.
  ```python
  def handle_input(grid):
      ...
  ```

## Future Improvements

- **Pattern Saving and Loading**: Implement functionality to save and load specific cell configurations.
- **Speed Control**: Add controls to adjust the simulation speed.
- **Different Patterns**: Include preset patterns like gliders or blinkers.
- **Enhanced UI**: Improve the user interface with additional features or settings.

## Acknowledgements

This project was built using the `pygame` and `numpy` libraries, inspired by the cellular automata principles defined by John Conway.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
