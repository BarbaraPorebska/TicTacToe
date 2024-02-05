# TicTacToe

In this project your job is to implement Tic-Tac-Toe for two players. You also can try writing some AI to play the game. If you find it easy, try to make it unbeatable.

<b><br>Initialize the board</br></b>
Implement get_empty_board() to return an empty 3-by-3 board, a list of lists filled with dots. The inner lists are rows.

A list of lists is returned that represents a list of rows.

Every cell of the returned value is .

The rows of the returned value are independent, changing one row does not affect the others.

Printing the result of the get_empty_board() function shows the following in the terminal.

[ [ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ] ]

<b><br>Get players' move</br></b>
Implement get_human_coordinates that asks for user input and returns the coordinates of a valid move on board.

The accepts coordinates as a letter and a number: A2 is first row and second column, C1 is third row and first column, and so on.

The function returns a tuple of two integers (row, col).

The returned coordinates start from 0.

The integers indicate a valid (empty) position on the board.

The program keeps asking for coordinates if the coordinates provided are outside of board.

The program keeps asking for coordinates if the coordinates provided are taken.

The program keeps asking for coordinates if the coordinates provided do not match the format.


<b><br>Implement making a move</br></b>
When the user has chosen a coordinate, that place is marked on the board.

If the cell at row and col is empty (contains a dot .), it is marked with player.

Out-of-bounds coordinates are not interpreted as moves.

Coordinates of already occupied cells are not interpreted as moves.


<b><br>Check for winners</br></b>
Implement get_winning_player() that returns X or O based on the winning player has three of their marks in a horizontal, vertical, or diagonal row on board.

The get_winning_player() function returns X if X has a three-in-a-row on board.

The get_winning_player() function returns None if there is no three-in-a-row on the board


<b><br>Check for a full board</br></b>
Implement is_board_full that returns True if the board is full.

The is_board_full function returns True if there are no empty cells on the board.

The is_board_full() returns False if there are empty cells on the board.


<b><br>Print board</br></b>
Implement display_board() that prints the board to the screen.

Players are indicated with X and 0. Empty fields are indicated with dots (.).

Coordinates are displayed around the board.

The board is displayed in the following format:

1 2 3
A . | . | .
---+---+---
B . | . | .
---+---+---
C . | . | .

<b><br>Print result</br></b>
The game shows if X or O or no one has won the game

If player X wins, "X has won!" is displayed.

If player 0 wins, "0 has won!" is displayed.

If nobody wins, "It's a tie!" is displayed.


<b><br>Game logic</br></b>
Implement all the functions so that the game will run successfully

Player X starts the game.

Players alternate their moves (X, 0, X, 0...).

The board is displayed before each move, and at the end of game.

The game ends when someone wins or the board is full.
The game handles bad input (wrong coordinates) without crashing.



