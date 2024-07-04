# Tic Tac Toe Game with GUI

This repository contains two versions of a Tic Tac Toe game developed in Python using the `tkinter` library. 
The first version is a two-player game, and the second version includes an AI opponent.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology and Algorithms](#methodology-and-algorithms)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Overview

Tic Tac Toe is a classic game where two players take turns marking spaces in a 3x3 grid. 
The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Features

### Version 1: Two-Player Game

- Play against another human.
- Simple and intuitive GUI.
- Adjustable board size (3x3 to 10x10).

### Version 2: Player vs AI

- Play against an AI opponent.
- AI uses the minimax algorithm with alpha-beta pruning.
- Adjustable board size (3x3 to 10x10).
- AI move delay for a better user experience.

## Installation

### Prerequisites

- Python 3.x
- `tkinter` (comes pre-installed with Python on most systems)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-gui.git
   cd tic-tac-toe-gui
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Run the game:
   ```bash
   python tictactoe_two_player.py  # For the two-player version
   python tictactoe_with_ai.py     # For the AI version
   ```

## Usage

1. **Two-Player Game**:
   - Open a terminal and navigate to the project directory.
   - Run `python tictactoe_two_player.py`.
   - Use the buttons on the GUI to play the game.

2. **Player vs AI**:
   - Open a terminal and navigate to the project directory.
   - Run `python tictactoe_with_ai.py`.
   - Use the buttons on the GUI to play against the AI.

### Adjustable Board Size

- Use the "Set Board Size" option in the menu to adjust the board size from 3x3 to 10x10.
- The AI's performance is optimized for smaller board sizes.

## Methodology and Algorithms

### Minimax Algorithm with Alpha-Beta Pruning

The AI in the Tic Tac Toe game uses the minimax algorithm with alpha-beta pruning to determine the best move. Here's a brief overview:

- **Minimax Algorithm**: A recursive algorithm used for decision-making in game theory.
- It evaluates all possible moves in the game to determine the best possible move for the AI by assuming that the opponent is also playing optimally.

- **Alpha-Beta Pruning**: An optimization technique for the minimax algorithm.
- It reduces the number of nodes evaluated by the minimax algorithm by pruning branches that cannot possibly influence the final decision.

The algorithm works as follows:
1. The AI evaluates all possible moves and their outcomes.
2. It assigns a score to each move: +10 for a win, -10 for a loss, and 0 for a draw.
3. It chooses the move with the highest score, assuming the opponent is also trying to maximize their score.
4. Alpha-beta pruning helps skip unnecessary evaluations, improving performance.

### AI Move Delay

To improve the user experience, a delay of 0.5 seconds is introduced before the AI makes its move. 
This is achieved using the `after` method in `tkinter`, which schedules a function to be called after a given amount of time.

## Screenshots

![image](https://github.com/GZ-Starter/Tic-tac-Toe/assets/126936908/34b10ffa-bdb8-4c73-badf-c637d1eb4810)  
*Description: A screenshot of the two-player Tic Tac Toe game.*  

![image](https://github.com/GZ-Starter/Tic-tac-Toe/assets/126936908/a872e6c8-7fb3-440d-b011-ce353c3919a8)  
*Description: A screenshot of the Tic Tac Toe game with AI.*

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
