#Initalize Board
g1 = " "
g2 = " "
g3 = " "
g4 = " "
g5 = " "
g6 = " "
g7 = " "
g8 = " "
g9 = " "

#Variables to check game status and current player (good)
is_gameover = False
current_mark = "X"

#Starting grid
def print_number_grid(): 
    print(f"1|2|3")
    print(f"4|5|6")
    print(f"7|8|9")

#Ingame grid
def print_grid():
    print(f"{g1}|{g2}|{g3}")
    print(f"{g4}|{g5}|{g6}")
    print(f"{g7}|{g8}|{g9}")

def check_gameover(mark):
    # X Horizontal wins
    global is_gameover
    if (g1 == g2 == g3 == mark) or (g4 == g5 == g6 == mark) or (g7 == g8 == g9 == mark):
        is_gameover = True
        return True
    
    # X Vertical wins
    if (g1 == g4 == g7 == mark) or (g2 == g5 == g8 == mark) or (g3 == g6 == g9 == mark):
        is_gameover = True
        return True
    
    # X Diagonal wins
    if (g1 == g5 == g9 == mark) or (g7 == g5 == g3 == mark):
        is_gameover = True
        return True

#Check if player is ready to start
start_input = input("Welcome to Tic-Tac-Toe, are you ready to start? (Y\\n) ")

if start_input in ["y", "Y", "yes", "Yes", "YES"]:
    print_number_grid()
elif start_input in ["n", "N", "no", "No", "NO"]:
    print("Your loss!")

#In-game while loop
while is_gameover == False:
    game_input = input(f"\nPlayer {current_mark}'s Turn:")

    #Check if move is valid (0-9)
    while int(game_input) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        game_input = input("Invalid input, please enter a valid number from 1-9\n")

    #Check if move is in empty spot, if so then change to current_mark
    is_placed = False
    while is_placed == False:
        match int(game_input):
            case 1:
                if g1 != "X" and g1 != "O":
                    g1 = current_mark
                    is_placed = True
            case 2:
                if g2 != "X" and g2 != "O":
                    g2 = current_mark
                    is_placed = True
            case 3:
                if g3 != "X" and g3 != "O":
                    g3 = current_mark
                    is_placed = True
            case 4:
                if g4 != "X" and g4 != "O":
                    g4 = current_mark
                    is_placed = True
            case 5:
                if g5 != "X" and g5 != "O":
                    g5 = current_mark
                    is_placed = True
            case 6:
                if g6 != "X" and g6 != "O":
                    g6 = current_mark
                    is_placed = True
            case 7:
                if g7 != "X" and g7 != "O":
                    g7 = current_mark
                    is_placed = True
            case 8:
                if g8 != "X" and g8 != "O":
                    g8 = current_mark
                    is_placed = True
            case 9:
                if g9 != "X" and g9 != "O":
                    g9 = current_mark
                    is_placed = True
        if is_placed is False:
            game_input = input("Invalid input, please pick a grid space that has not been marked already and a valid number between 1-9\n")
    is_placed = False

    print_grid()

    #Check if there is winner
    if check_gameover(current_mark):
        print(f"Player {current_mark} wins!")
    
    #Alternate player turns
    if current_mark == "X":
        current_mark = "O"
    else:
        current_mark = "X"