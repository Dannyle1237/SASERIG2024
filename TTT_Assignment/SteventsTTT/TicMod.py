#Initalize Board
#Modify: Why not use a list from 0-8? Less confusing than dict 
#Before: 
#spots = {1: '1', 2: '2',3: '3', 4:'4',5: '5',6:'6',7:'7',8:'8',9:'9'}
#After:
spots = list(range(10)) # range(10) returns immutable list [0,1,2,3,4,5,6,7,8,9]. We cast to list() to make it mutable

#Function to print board 
def draw_board(spots):
    #Before
    #board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"f"|{spots[7]}|{spots[8]}|{spots[9]}|\n")
    #After: Removing extra fs
    board = (f"|{spots[0]}||{spots[1]}||{spots[2]}|\n|{spots[3]}||{spots[4]}||{spots[5]}|\n|{spots[6]}||{spots[7]}||{spots[8]}|")
    print (board)

#Variables (game status and player turn (0=X,1=O))
playing = True
#We can change turn to represent the player turn's character('X', 'O')
#Easier to read and understand what is stored in variable
turn = 'X'

#Runtime code

#In-game loop 
while playing:
    #VVV Moved from top to here
    draw_board(spots)

    #Take player input
    choice = int(input("Enter number from 0-8 here: ")) #Added words to make more sense

    #Modify board based on player input
    #Before: Switch case was repetitive and hard to read
    # match int(choice):
    #     case 1: #Find player's input
    #         if spots[1] == '1': #check if spot is not taken
    #             if turn%2 == 0: #No longer need to check turn since our turn variable = character
    #                 spots[1]="X" #Now we can do spot = turn
    #                 draw_board(spots) #redraw board
    #                 turn = turn + 1 #Turn changes to opposite
    #             else:
    #                 spots[1]="O" #Repeat of above block
    #                 draw_board(spots)
    #                 turn = turn + 1
    #         else: #Invalid case (Spot is already taken)
    #             print("Pick another number")
    #             draw_board(spots) #Move drawboard to beginning of while loop
    
    #After:
    #Find player's input (Already stored in input)
    if choice in range(10): #Check if player's input is valid (0-9)
        if spots[choice] == choice: #check if spot is not taken
            spots[choice] = turn #If spot is available, change to variable turn (X or O) 
            #Now we check for winner
            #Winner is determined if spots from current turn create a horizontal/vertical line or diagonal
            
            #Check horizontal lines (0,1,2)(3,4,5)(6,7,8) <- forloopable
            for num in [0,3,6]:
                if turn == spots[num] == spots[num+1] == spots[num+2]:
                #Better way if spots[num:num+3] == [turn,turn,turn]:
                    print(f"Winner is Player {turn}")
                    playing = False
            
            #Check vertical lines (0,3,6)(1,4,7)(2,5,8)
            for num in range(3): #list [0,1,2]
                if turn == spots[num] == spots[num+3] == spots[num+6]:
                    print(f"Winner is {turn}")
                    playing = False

            #Check diagonals (0,4,8)(2,4,6)
            #middle (spot 4) is required 
            if turn == spots[4]:
                #check corners
                if (turn == spots[0] == spots[8]) or (turn == spots[2] == spots[6]):
                    print(f"Winner is {turn}")
                    playing = False

            #No winner = continue with game
            if turn == 'X':#Turn changes to opposite
                turn = 'O'
            else:
                turn = 'X'
        else: #Spot is already taken, invalid move
            print("Move is invalid, spot is already taken. Please choose another")
    else: #If input was not 0-9
        print("Invalid input, please enter number between 0-9")

    #Check for winners
    #Before: Hard coded checks. Think about in mathematical way
    #Also best to check if there is winner after a VALID move is played. otherwise waste of runtime
    # if spots[1] =="X" and spots[2] == "X" and spots[3] == "X":
    #     print("X wins") print winner
    #     break (Instead change while loop condition to false.)
    # if spots[4] == "X" and spots[5] == "X" and spots[6] == "X":
    #     print("X wins")
    #     break
    # if spots[7] =="X" and spots[8] == "X" and spots[9] == "X":
    #     print("X wins")
    #     break
    # if spots[1] =="X" and spots[4] == "X" and spots[7] == "X":
    #     print("X wins")
    #     break
    # if spots[2] == "X" and spots[5] == "X" and spots[8] == "X":
    #     print("X wins")
    #     break
    # if spots[3] =="X" and spots[6] == "X" and spots[9] == "X":
    #     print("X wins")
    #     break
    # if spots[1] =="X" and spots[5] == "X" and spots[9] == "X":
    #     print("X wins")
    #     break
    # if spots[3] == "X" and spots[5] == "X" and spots[7] == "X":
    #     print("X wins")
    #     break

    # if spots[1] =="O" and spots[2] == "O" and spots[3] == "O":
    #     print("O wins")
    #     break
    # if spots[4] == "O" and spots[5] == "O" and spots[6] == "O":
    #     print("O wins")
    #     break
    # if spots[7] =="O" and spots[8] == "O" and spots[9] == "O":
    #     print("O wins")
    #     break
    # if spots[1] =="O" and spots[4] == "O" and spots[7] == "O":
    #     print("O wins")
    #     break
    # if spots[2] == "O" and spots[5] == "O" and spots[8] == "O":
    #     print("O wins")
    #     break
    # if spots[3] =="O" and spots[6] == "O" and spots[9] == "O":
    #     print("O wins")
    #     break
    # if spots[1] =="O" and spots[5] == "O" and spots[9] == "O":
    #     print("O wins")
    #     break
    # if spots[3] == "O" and spots[5] == "O" and spots[7] == "O":
    #     print("O wins")
    #     break
    # if turn > 8:
    #     print("Tie")
    #     break
    
#Draw winning board
draw_board(spots)