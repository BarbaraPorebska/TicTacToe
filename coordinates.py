import sys
import random
from board import is_board_full, get_winning_player
from copy import deepcopy


def get_human_coordinates(board, current_player):
    """
    Should return the read coordinates for the tic tac toe board from the terminal.
    The coordinates should be in the format  letter, number where the letter is
    A, B or C and the number 1, 2 or 3.
    If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf)
    than a warning message should appear and the coordinates reading process repeated.
    If the user enters a coordinate that is already taken on the board.
    than a warning message should appear and the coordinates reading process repeated.
    If the user enters the word "quit" in any format of capitalized letters the program
    should stop.
    """

    valid_letters = ["A", "B", "C"]
    valid_numbers = ["1", "2", "3"]

    while True:
        user_input = input("Please enter your move: ")

        if user_input.upper() == "QUIT":
            sys.exit()

        if (
            len(user_input) == 2
            and user_input[0].upper() in valid_letters
            and user_input[1] in valid_numbers
        ):
            if (
                board[valid_letters.index(user_input[0].upper())][
                    valid_numbers.index(user_input[1])
                ]
                == "."
            ):
                return (
                    valid_letters.index(user_input[0].upper()),
                    valid_numbers.index(user_input[1]),
                )
            else:
                print("This coordinate is already taken.")
        else:
            print("Invalid coordinate")


def get_random_ai_coordinates(board, current_player):
    """
    Should return a tuple of 2 numbers.
    Each number should be between 0-2.
    The chosen number should be only a free coordinate from the board.
    If the board is full (all spots taken by either X or O) than "None"
    should be returned.
    """

    if is_board_full(board):
        return None

    moves = get_possible_moves(board)

    # checking for winning move
    for move in moves:
        temp_board = deepcopy(board)
        temp_board[move[0]][move[1]] = current_player
        if get_winning_player(temp_board) == current_player:
            return move

    # checking for opponent's winning move
    match current_player:
        case "X":
            opponent = "O"
        case "O":
            opponent = "X"

    for move in moves:
        temp_board = deepcopy(board)
        temp_board[move[0]][move[1]] = opponent
        if get_winning_player(temp_board) == opponent:
            return move

    return random.choice(moves)


def get_unbeatable_ai_coordinates(board, current_player):
    """
    Should return a tuple of 2 numbers.
    Each number should be between 0-2.
    The chosen number should be only a free coordinate from the board.
    The chosen coordinate should always stop the other player from winning or
    maximize the current player's chances to win.
    If the board is full (all spots taken by either X or O) than "None"
    should be returned.
    """


def score_move(board, current_player):
    if get_winning_player(board) == current_player:
        return 1
    elif get_winning_player(board) == None:
        return 0
    else:
        return -1


def get_possible_moves(board):
    temp = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ".":
                temp.append((i, j))
    return temp


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    board_1 = [
        ["X", "X", "."],
        ["X", ".", "."],
        ["X", "X", "."],
    ]
    print("It should print the coordinates selected by the human player")
    coordinates = get_human_coordinates(board_1, "X")
    print(coordinates)

    board_2 = [
        ["O", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2, "X"))
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2, "X"))
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2, "X"))

    board_3 = [
        ["O", "X", "X"],
        ["X", "O", "X"],
        ["X", "O", "X"],
    ]
    print("The printed coordinate should be None")
    print(get_random_ai_coordinates(board_3))

    board_4 = [
        [".", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("The printed coordinate should always be (0, 0)")
    print(get_unbeatable_ai_coordinates(board_4, "X"))

    board_5 = [
        ["X", "O", "."],
        ["X", ".", "."],
        ["O", "O", "X"],
    ]
    print("The printed coordinate should always be (1, 1)")
    print(get_unbeatable_ai_coordinates(board_5, "O"))

    board_6 = [
        ["O", "O", "."],
        ["O", "X", "."],
        [".", "X", "."],
    ]
    print("The printed coordinate should either (0, 2) or (2, 0)")
    print(get_unbeatable_ai_coordinates(board_6))
