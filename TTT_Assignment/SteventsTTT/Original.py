spots = {1: '1', 2: '2',3: '3', 4:'4',5: '5',6:'6',7:'7',8:'8',9:'9'}
def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"f"|{spots[7]}|{spots[8]}|{spots[9]}|\n")
    print (board)
draw_board(spots)
playing =  True
turn = 0
while playing:
    choice = input()
    match int(choice):

        case 1:
            if spots[1] == '1':
                if turn%2 == 0:
                    spots[1]="X"
                    draw_board(spots)
                    turn = turn + 1
                else:
                    spots[1]="O"
                    draw_board(spots)
                    turn = turn + 1
            else:
                print("Pick another number")
                draw_board(spots)
        case 2:
            if spots[2] == '2':
                if turn%2 == 0:
                    spots[2]="X"
                    draw_board(spots)
                    turn = turn + 1
                else:
                    spots[2]="O"
                    draw_board(spots)
                    turn = turn + 1
            else:
                print("Pick another number")
                draw_board(spots)
        case 3:
            if spots[3] == '3':
                if turn%2 == 0:
                    spots[3]="X"
                    draw_board(spots)
                    turn = turn + 1
                else:
                    spots[3]="O"
                    draw_board(spots)
                    turn = turn + 1
            else:
                print("Pick another number")
                draw_board(spots)
        case 4:
            if spots[4] == '4':
                if turn%2 == 0:
                    spots[4]="X"
                    draw_board(spots)
                    turn = turn + 1
                else:
                    spots[4]="O"
                    draw_board(spots)
                    turn = turn + 1
            else:
                print("Pick another number")
                draw_board(spots)
        case 5:
            if spots[5] == '5':
                if turn%2 == 0:
                    spots[5]="X"
                    draw_board(spots)
                    turn = turn + 1
                else:
                    spots[5]="O"
                    draw_board(spots)
                    turn = turn + 1
            else:
                print("Pick another number")
                draw_board(spots)
        case 6:
            if spots[6] == '6':
                if turn%2 == 0:
                    spots[6]="X"
                    draw_board(spots)
                    turn = turn + 1
                else:
                    spots[6]="O"
                    draw_board(spots)
                    turn = turn + 1
            else:
                print("Pick another number")
                draw_board(spots)
        case 7:
            if spots[7] == '7':
                if turn%2 == 0:
                    spots[7]="X"
                    draw_board(spots)
                    turn = turn + 1
                else:
                    spots[7]="O"
                    draw_board(spots)
                    turn = turn + 1
            else:
                print("Pick another number")
                draw_board(spots)
        case 8:
            if spots[8] == '8':
                if turn%2 == 0:
                    spots[8]="X"
                    draw_board(spots)
                    turn = turn + 1
                else:
                    spots[8]="O"
                    draw_board(spots)
                    turn = turn + 1
            else:
                print("Pick another number")
                draw_board(spots)
        case 9:
            if spots[9] == '9':
                if turn%2 == 0:
                    spots[9]="X"
                    draw_board(spots)
                    turn = turn + 1
                else:
                    spots[9]="O"
                    draw_board(spots)
                    turn = turn + 1
            else:
                print("Pick another number")
                draw_board(spots)
        case default:
            print("Please Enter 1-9")
            draw_board(spots)
    if spots[1] =="X" and spots[2] == "X" and spots[3] == "X":
        print("X wins")
        break
    if spots[4] == "X" and spots[5] == "X" and spots[6] == "X":
        print("X wins")
        break
    if spots[7] =="X" and spots[8] == "X" and spots[9] == "X":
        print("X wins")
        break
    if spots[1] =="X" and spots[4] == "X" and spots[7] == "X":
        print("X wins")
        break
    if spots[2] == "X" and spots[5] == "X" and spots[8] == "X":
        print("X wins")
        break
    if spots[3] =="X" and spots[6] == "X" and spots[9] == "X":
        print("X wins")
        break
    if spots[1] =="X" and spots[5] == "X" and spots[9] == "X":
        print("X wins")
        break
    if spots[3] == "X" and spots[5] == "X" and spots[7] == "X":
        print("X wins")
        break

    if spots[1] =="O" and spots[2] == "O" and spots[3] == "O":
        print("O wins")
        break
    if spots[4] == "O" and spots[5] == "O" and spots[6] == "O":
        print("O wins")
        break
    if spots[7] =="O" and spots[8] == "O" and spots[9] == "O":
        print("O wins")
        break
    if spots[1] =="O" and spots[4] == "O" and spots[7] == "O":
        print("O wins")
        break
    if spots[2] == "O" and spots[5] == "O" and spots[8] == "O":
        print("O wins")
        break
    if spots[3] =="O" and spots[6] == "O" and spots[9] == "O":
        print("O wins")
        break
    if spots[1] =="O" and spots[5] == "O" and spots[9] == "O":
        print("O wins")
        break
    if spots[3] == "O" and spots[5] == "O" and spots[7] == "O":
        print("O wins")
        break
    if turn > 8:
        print("Tie")
        break
draw_board(spots)