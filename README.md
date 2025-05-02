## TO Run the Game
Download the Files and folders as it is and run chess.py to play the game.


## References:
* Program Uses pygame: http://www.pygame.org/

  * Chess tile graphics were used from Wikimedia Commons: http://commons.wikimedia.org/wiki/File:Chess_tile_pd.png

  * alphaBeta Function was created based on the pseudocode Provided by wikipedia: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning


  * Generating Move lists for each piece class was inspired by chessprogramming wikispace on move lists: https://chessprogramming.wikispaces.com/Move%20List

  * Board representation 'boardArray' is based off the 8x8 board array method: https://chessprogramming.wikispaces.com/8x8%20Board

  * Chess.com for descriptions of basic and special moves pieces can make:
  https://www.chess.com/learn-how-to-play-chess

Pychess: A Pygame-Based Chess Engine with AI

Pychess is a chess game built using Pygame that allows players to play against an AI that autonomously makes its moves. The game utilizes a class-based structure and polymorphism for managing the chessboard and pieces.

## Key Features:

Board Class:

Contains all the necessary functions for the chessboard, including handling piece movements and detecting whether the player or AI is in check.
Piece Classes:

Each chess piece has its own class, derived from an abstract Piece class. These classes encapsulate piece-specific movement logic, ensuring accurate behavior on the board.
Special Moves:

Promotions: When a pawn reaches the opponent’s back rank, it can promote to a queen, rook, bishop, or knight.
Castling: A player can perform castling, moving the king two squares and positioning the rook beside it.
AI Using Alpha-Beta Pruning:

The AI evaluates possible moves using the Alpha-Beta Pruning Search Algorithm, an optimized version of the Minimax Algorithm.
This algorithm helps the AI decide the best possible move by pruning branches in the decision tree that will not affect the final decision, improving efficiency and reducing search time.
## Alpha-Beta Pruning Overview:

Alpha-Beta Pruning optimizes decision-making by maintaining two values, alpha and beta, representing the best scores for the maximizing and minimizing players, respectively.
The AI evaluates moves up to a maximum depth of 3 plies by default, though this can be adjusted to 4 plies for deeper analysis (which increases the computation time).
When the algorithm detects that further exploration of a branch will not lead to a better outcome, it prunes that branch.
## Game Components:

Assets Folder: Contains sprite images for chess pieces used in the graphical interface.
chess.py: Main program to run the game interface and start the game.
board.py: Contains the Board class and the Alpha-Beta pruning logic.
pieces.py: Contains the abstract Piece class, along with specific classes for each type of piece (e.g., pawn, rook, knight, etc.).
ratings.py: Implements a Rating class used to evaluate the quality of moves based on multiple criteria.
userInterface.py: Handles the graphical user interface with Pygame, allowing the player to make moves with the mouse and interact with the game.
Evaluation and Performance:

The main objective of the project is to ensure that the AI generates optimal moves quickly. During testing, the AI typically takes less than 1 second per move.
The AI’s performance can be observed by checking the time it takes to make each move, which is printed after every AI move.
Move Validation:

The project ensures that each piece adheres to its specific movement rules. The rules for each piece are described in detail in the project's documentation and can be manually tested by moving pieces on the board.
Customizing Depth:

By default, the maximum search depth for the AI is set to 3 plies, but this can be adjusted in the board.py file. To change the search depth, simply modify the MAXDEPTH variable in the Board class constructor (e.g., self.MAXDEPTH = 4) for deeper moves at the cost of longer computation time.
