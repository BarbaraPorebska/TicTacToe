def get_empty_board():
    empty_board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return empty_board

    """
    Should return a list with 3 sublists.
    Each sublist should contain 3 time the "." character
    """


def display_board(board):
    board = f"""
    1   2   3
 A  {board[0][0]} | {board[0][1]} | {board[0][2]} 
   ---+---+---
 B  {board[1][0]} | {board[1][1]} | {board[1][2]}
   ---+---+---
 C  {board[2][0]} | {board[2][1]} | {board[2][2]} 
   ---+---+---
"""
    print(board)


empty_board = get_empty_board()
display_board(empty_board)


"""
  Should print the tic tac toe board in a format similar to

       1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       --+---+---
    C   0 | X | . 
       --+---+---
  """


def is_board_full(board):
    if any("." in i for i in board):
        return False
    else:
        return True

    """
  should return True if there are no more empty place on the board,
  otherwise should return False
  """


def get_winning_player(board):
    """
    Should return the player that wins based on the tic tac toe rules.
    If no player has won, than "None" is returned.
    """
    # checking horizontals
    for i in range(len(board)):
        if (
            not board[i][0] == "."
            and board[i][0] == board[i][1]
            and board[i][1] == board[i][2]
        ):
            return board[i][0]

    # checking verticals
    for i in range(len(board)):
        if (
            not board[0][i] == "."
            and board[0][i] == board[1][i]
            and board[1][i] == board[2][i]
        ):
            return board[0][i]

    # checking diagonals
    if (
        not board[0][0] == "."
        and board[0][0] == board[1][1]
        and board[1][1] == board[2][2]
    ):
        return board[0][0]
    elif (
        not board[0][2] == "."
        and board[0][2] == board[1][1]
        and board[1][1] == board[2][0]
    ):
        return board[0][2]

    return None


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    empty_board = get_empty_board()
    print(empty_board)

    board = [["X", "O", "."], ["X", "O", "."], ["0", "X", "."]]
    print(
        """
    should print 
        1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       ---+---+---
    C   0 | X | . 
       ---+---+---
    """
    )

    display_board(board)

    board_1 = [
        ["X", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("Should return False")
    print(is_board_full(board_1))

    board_2 = [
        [".", "O", "O"],
        [".", "O", "X"],
        [".", "X", "X"],
    ]
    print("Should return False")
    print(is_board_full(board_2))

    board_3 = [
        ["O", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "X"],
    ]
    print("Should return True")
    print(is_board_full(board_3))

    board_4 = [
        ["X", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("Should return X")
    print(get_winning_player(board_4))

    board_5 = [
        ["X", "O", "O"],
        ["X", "O", "."],
        ["O", "X", "X"],
    ]
    print("Should return O")
    print(get_winning_player(board_5))

    board_6 = [
        ["O", "O", "."],
        ["O", "X", "."],
        [".", "X", "."],
    ]
    print("Should return None")
    print(get_winning_player(board_6))
