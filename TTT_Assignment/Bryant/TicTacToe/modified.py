import os

#Took all functions and code into one file, just for simplicity. 

#renamed func/variables to be more clear. also removed extra fs.
def printBoard(board):
    board = (f"+---+---+---+\n| {board[1]} | {board[2]} | {board[3]} |\n+---+---+---+\n| {board[4]} | {board[5]} | {board[6]} |\n+---+---+---+\n| {board[7]} | {board[8]} | {board[9]} |\n+---+---+---+")
    print(board)

#Function that converts value of turn (a number) to it's corresponding letter ('O' or 'X')
def checkTurn(turn):
    if turn % 2 == 0: 
        return 'O'
    else: 
        return 'X'

def checkwin(spotonboard): 
    if (spotonboard[1] == spotonboard[2] == spotonboard[3]) \
    or (spotonboard[4] == spotonboard[5] == spotonboard[6]) \
    or (spotonboard[7] == spotonboard[8] == spotonboard[9]):
        return True
    
    elif (spotonboard[1] == spotonboard[4] == spotonboard[7]) \
    or (spotonboard[2] == spotonboard[5] == spotonboard[8]) \
    or (spotonboard[3] == spotonboard[6] == spotonboard[9]):
        return True
    
    elif (spotonboard[1] == spotonboard[5] == spotonboard[9]) \
    or (spotonboard[7] == spotonboard[5] == spotonboard[3]):
        return True
    else: return False


#Dict to represent game board (Could be renamed to just board, spotonboard sounds like a single spot)
board = {1 : '1', 2 : '2', 3 : '3',
        4 : '4', 5 : '5', 6 : '6', 
        7 : '7', 8 : '8', 9 : '9'}

#Variables
#In-game status (renamed to is_playing)
is_playing = True

#Track current turn (Even and 0 = 'X' and Odd = 'O')
turn = 0

# Removed cause no longer needed w/ checkWin
# complete = 0

#Track previous turn
prev_turn = -1

while is_playing:
    #Line of code to clear console screeen
    os.system('cls' if os.name == 'nt' else 'clear')

    #show board
    printBoard(board)

    #Check if turn is the same (Player placed invalid input)
    if prev_turn == turn:
        print("Spot not Available")

    prev_turn = turn

    #turn%2 + 1 prints player 1 or 2's turn.
    print("Player " + str((turn % 2) + 1) + "'s turn: ") 

    #Obtain player input
    choice = input("Enter choice here: ")

    #Option to exit game
    if choice == 'q' or choice == 'quit': 
        break

    #Here we check early if choice isdigit, then cast if valid to avoid repeatedly casting
    if(choice.isdigit()):
        choice = int(choice)
        if choice in board:
            #Could also do board[choice] != choice. Your way is fine though, just an alternative
            if board[choice] not in {"X", "O"}:
                #Change to next players turn
                turn += 1
                board[choice] = checkTurn(turn)
            
        #Check for a winner, if so end game
        if checkwin(board):
            is_playing = False
            os.system('cls' if os.name == 'nt' else 'clear')
            printBoard(board)
            if checkTurn(turn) == 'X':
                print("Player 1 wins")
            else:
                print("Player 2 wins")
            
        #All spots on board are filled means end game
        if turn > 8:
            is_playing = False
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Game Over")



