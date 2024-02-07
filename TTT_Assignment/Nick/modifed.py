#Initalize Board
#Before: 9 different variables = 9 different memory allocations
# g1 = " "
# g2 = " "
# g3 = " "
# g4 = " "
# g5 = " "
# g6 = " "
# g7 = " "
# g8 = " "
# g9 = " "
#After 
#Please ensure that variables are named in a way that clearly conveys their purpose or meaning
grid = [" "," "," "," "," "," "," "," "," "] #List to store 9 values

#Variables to check game status and current player (good)
is_gameover = False
current_mark = "X"

#Starting grid
#After: Changed to 0-8 to better match w/ array indexes
#       Could also just add one to index if want to keep 1-9
def print_number_grid(): 
    print(f"0|1|2")
    print(f"3|4|5")
    print(f"6|7|8")

#Ingame grid w/ empty slots
def print_grid():
    print(f"{grid[0]}|{grid[1]}|{grid[2]}")
    print(f"{grid[3]}|{grid[4]}|{grid[5]}")
    print(f"{grid[6]}|{grid[7]}|{grid[8]}")

def check_gameover(mark):
    # X Horizontal wins
    global is_gameover
    if (grid[0] == grid[1] == grid[2] == mark) or (grid[3] == grid[4] == grid[5] == mark) or (grid[6] == grid[7] == grid[8] == mark):
        is_gameover = True
        return True
    
    # X Vertical wins
    if (grid[0] == grid[3] == grid[6] == mark) or (grid[1] == grid[4] == grid[7] == mark) or (grid[2] == grid[5] == grid[8] == mark):
        is_gameover = True
        return True
    
    # X Diagonal wins
    if (grid[0] == grid[4] == grid[8] == mark) or (grid[6] == grid[4] == grid[2] == mark):
        is_gameover = True
        return True

#Check if player is ready to start
start_input = input("Welcome to Tic-Tac-Toe, are you ready to start? (Y\\n) ")

if start_input in ["y", "Y", "yes", "Yes", "YES"]:
    print_number_grid()
elif start_input in ["n", "N", "no", "No", "NO"]:
    print("Your loss!")

#In-game while loop
#Before:
#while is_gameover == False:
#After:
while not is_gameover:
    #Automatically store input as int to avoid headache
    game_input = int(input(f"\nPlayer {current_mark}'s Turn:"))

    #Check if move is valid (0-8)
    while game_input not in range(9): #range returns immutable list [0,1,2,3,4,5,6,7,8]
        game_input = int(input("Invalid input, please enter a valid number from 0-8\n"))

    #Check if move is in empty spot, if so then change to current_mark
    #Before: While loop w/ switch statement
    # is_placed = False
    # while is_placed == False: #While loop runs till valid move is played
    #     match int(game_input):
    #         case 1:
    #             if g1 != "X" and g1 != "O": #Check if spot is taken
    #                 g1 = current_mark #Replace spot w/ mark
    #                 is_placed = True
    #     if is_placed is False: #Ask for reinput if invalid move
    #     game_input = input("Invalid input, please pick a grid space that has not been marked already and a valid number between 1-9\n")
    #After:
    #While loop checking till valid move is played
    is_placed = False
    while not is_placed:
        #check if spot is taken
        if( grid[game_input] == " "):
            grid[game_input] = current_mark
            is_placed = True
        else: #Ask for reinput if invalid move
            game_input = int(input("Invalid input, please pick a grid space that has not been marked already and a valid number between 1-9\n"))
    print_grid()

    #Check if there is winner
    if check_gameover(current_mark):
        print(f"Player {current_mark} wins!")
    
    #Alternate player turns
    if current_mark == "X":
        current_mark = "O"
    else:
        current_mark = "X"