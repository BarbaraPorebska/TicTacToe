import sys

def get_menu_option():
    while True:
        menu = input("Please choose game mode:\n 1. Human vs Human\n 2. Random AI vs Random AI\n 3. Human vs Random AI\n 4. Human vs Unbeatable AI\n")
        if menu.lower() == "quit":
            sys.exit()
        try:
            if int(menu) > 0 and int(menu) <= 4:
                return menu
            else:
                print("\nPlease choose a number between 1 and 4\n")
        except ValueError:
            print("\nPlease enter a number\n")


    
'''
  Should print a menu with the following options:
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
  '''
pass


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print("If the user selected 1, it should print 1")
    print(option) 