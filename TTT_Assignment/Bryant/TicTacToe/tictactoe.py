from tictactoedict import board, checkturn, checkwin
import os

spotonboard = [1,2,3,'X',5,6,7,8,9]
              #idx start at 0

playing = 1
turn = 0
complete = 0
prev_turn = -1

while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    board(spotonboard)
    if prev_turn == turn:
        print("Spot not Available")
    prev_turn = turn
    print("Player " + str((turn % 2) + 1) + "'s turn: ") 
    choice = input()
    if choice == 'q' or choice == 'quit': 
        break
    elif choice.isdigit() and int(choice) in spotonboard:
        if spotonboard[int(choice)] not in {"X", "O"}:
            turn += 1
            spotonboard[int(choice)] = checkturn(turn)

    if checkwin(spotonboard):
        playing, complete = 0, 1
    if turn > 8:
        playing = 0
        print

os.system('cls' if os.name == 'nt' else 'clear')
board(spotonboard)

if complete:
    if checkturn(turn) == 'X':
        print("Player 1 wins")
    else:
        print("Player 2 wins")
else:
    print("Game Over")
