from tictactoedict import board, checkturn, checkwin
import os

#Dict to represent game board (Could be renamed to just board, spotonboard sounds like a single spot)
spotonboard = {1 : '1', 2 : '2', 3 : '3',
               4 : '4', 5 : '5', 6 : '6', 
               7 : '7', 8 : '8', 9 : '9'}

#Variables
#In-game status (Use True or False instead of 0 or 1)
playing = True

#Turns (Even and 0 = 'X' and Odd = 'O')
turn = 0

#Variable to check if game is done?
complete = 0

#Track previous turn
prev_turn = -1

while playing:
    #Line of code to clear console screeen
    os.system('cls' if os.name == 'nt' else 'clear')

    #show board
    board(spotonboard)

    if prev_turn == turn:
        print("Spot not Available")

    prev_turn = turn

    #turn%2 + 1 prints player 1 or 2's turn.
    print("Player " + str((turn % 2) + 1) + "'s turn: ") 

    #Obtain player input
    choice = input()

    #Option to exit game
    if choice == 'q' or choice == 'quit': 
        break
    #Check if choice is valid number (1-9) -- No need for isdigit() since the keys in spotonboard are digits.
    elif choice.isdigit() and int(choice) in spotonboard:

        #Could also do spotonboard[choice] != choice. Your way is fine though, just an alternative
        if spotonboard[int(choice)] not in {"X", "O"}:
            #Change to next players turn
            turn += 1
            spotonboard[int(choice)] = checkturn(turn)
    #Check for a winner, if so end game
    if checkwin(spotonboard):
        playing, complete = 0, 1
    #All spots on board are filled means end game
    if turn > 8:
        playing = 0
        #Mistype?
        print

os.system('cls' if os.name == 'nt' else 'clear')

board(spotonboard)

#Could create this part when you check for winner or check if spots are filled
if complete:
    if checkturn(turn) == 'X':
        print("Player 1 wins")
    else:
        print("Player 2 wins")
else:
    print("Game Over")
