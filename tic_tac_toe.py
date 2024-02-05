from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option
import time
import os
import sys


HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def play_again():
    while True:
        input_play_again = input("Do you want play again? [y/n] ")
        if input_play_again == "y":
            clear_screen()
            main()
        elif input_play_again == "n":
            print("Thanks for game! Bye.")
            sys.exit()
        else:
            print("Please type 'y' - yes or 'n' - no ")

def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    is_game_running = True
    change_sign = True

    while is_game_running:
        clear_screen()
        display_board(board)
        
        ### TO DO ###
        # in each new iteration of the while loop the program should 
        # alternate the value of `current_player` from `X` to `O`
        if change_sign:
            current_player = "X"
            change_sign = False
        else:
            current_player = "O"
            change_sign = True
        
        ### TO DO ###
        # based on the value of the variables `game_mode` and `current_player` 
        # the programm should should choose betwen the functions
        # get_random_ai_coordinates or get_umbeatable_ai_coordinates or get_human_coordinates

        match game_mode:
            case "1":
                x, y = get_human_coordinates(board, current_player)
            case "2":
                x, y = get_random_ai_coordinates(board, current_player)
                time.sleep(1.5)
            case "3":
                if change_sign:
                    x, y = get_random_ai_coordinates(board, current_player)
                    time.sleep(1.5)
                else:
                    x, y = get_human_coordinates(board, current_player)
            case "4":
                if change_sign:
                    x, y = get_human_coordinates(board, current_player)
                else:
                    x, y = get_unbeatable_ai_coordinates(board, current_player)
                    time.sleep(1.5)

        board[x][y] = current_player
        
        ### TO DO ###
        # based on the values of `winning_player` and `its_a_tie` the program
        # should either stop displaying a winning/tie message 
        # OR continue the while loop
        winning_player = get_winning_player(board)
        its_a_tie = is_board_full(board)

        if winning_player == "O":
            clear_screen()
            display_board(board)
            print("O has won!")
            play_again()
        elif winning_player == "X":
            clear_screen()
            display_board(board)
            print("X has won!")
            play_again()
        if its_a_tie:
            clear_screen()
            display_board(board)
            print("It's a tie!")
            play_again()    

if __name__ == "__main__":
    main()