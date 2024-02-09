def board(spotonboard):
    board = (f"+---+---+---+\n"
             f"| {spotonboard[1]} | {spotonboard[2]} | {spotonboard[3]} |\n"
             f"+---+---+---+\n"
             f"| {spotonboard[4]} | {spotonboard[5]} | {spotonboard[6]} |\n"
             f"+---+---+---+\n"
             f"| {spotonboard[7]} | {spotonboard[8]} | {spotonboard[9]} |\n"
             f"+---+---+---+")
    print(board)

def checkturn(turn):
    if turn % 2 == 0: 
        return 'O'
    else: 
        return "X"

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
