#returns the board after making a move
def play(board, block_no, player,mode):
    Turn = 0
    store_flag =0
    #2nd player playing
    block_no = block_no -1
    if (player):
        block_no = block_no+7 
        if (board [block_no] ==0 or block_no == 6 ):
            print("Enter a valid move")
            return board, player
        for i in range(board[block_no]):
            if ((block_no +i +1)%14 == 6):
               board[(block_no +i +2)%14] = board[(block_no +i +2)%14] +1
               store_flag = 1
            else:
                board[(block_no +i +1 +store_flag)%14] = board[(block_no +i +1 +store_flag)%14] +1
        #if he droped the last coin in his store,  play again
        if (((block_no +i +1 +store_flag)%14)==13):
            Turn =1
        else:
            Turn =0
        #stealing
        if(mode and (board[(block_no +i +1 +store_flag)%14] ==1) and ((block_no +i +1 +store_flag)%14 >6) and ((block_no +i +1 +store_flag)%14) != 13):
            board[13]= board[13] + 1 + board[(12-((block_no +i +store_flag)%14) )]
            board[(block_no +i +1 +store_flag)%14] =0
            board[(12-((block_no +i +store_flag)%14) )]=0
    
    #1st player playing
    else:
        if (board [block_no] ==0 or  block_no == 6):
            print("Enter a valid move")
            return board, player
        for i in range(board[block_no]):
            if ((block_no +i +1)%14 == 13):
                board[(block_no +i +2)%14] = board[(block_no +i +2)%14] +1
                store_flag = 1
            else:
                board[(block_no +i +1 +store_flag)%14] = board[(block_no +i +1 +store_flag)%14] +1
        #if he droped the last coin in his store,  play again
        if (((block_no +i +1 +store_flag)%14) ==6):
            Turn =0
        else:
            Turn =1
        #stealing
        if(mode and (board[(block_no +i +1 +store_flag)%14] ==1) and ((block_no +i +1 +store_flag)%14 <6) and ((block_no +i +1 +store_flag)%14) != 6):
            board[6]= board[6] + 1 + board[(12-((block_no +i +1 +store_flag)%14) )]
            board[(12-((block_no +i +1 +store_flag)%14) )] =0
            board[(block_no +i +1 +store_flag)%14] =0
    board[block_no]=0


    return board, Turn


def get_empty_pockets(board, player):
    empty_pockets = []
    block_no_start=0
    if(player):
        block_no_start= 7
    for i in range(6):
        if (board[block_no_start + i] == 0):
            empty_pockets.append((i+1))
    return empty_pockets


#example, since player 0 is paying, he has empty pockets number 1,3,6 that's the return of the function
#board = [0,1,0,2,3,0,0  , 2,2,0,1,3,1,0]
#print(get_empty_pockets(board,0))


#when one side has no more moves (empty side in the board)
#this function returns the score (diff between the 2 stores and the winner)
#takes the player whose side of the board is non empty
def calc_score(board):
    count=0
    player2_flag =7
    for i in board[:6]:
        if i != 0:
            count =-1
            break
    if (count ==-1):
        player2_flag =0

    for i in range(6):
        board[player2_flag+6] =board[player2_flag+6] + board [i+player2_flag]
    diff = board[6] - board[13]
    if (diff <0):
        return abs(diff), 1
    elif (diff>0):
        return abs(diff), 0
    else: #draw
        return abs(diff), 2


def print_board(board):
    player2_board =board[::-1]
    print("player2:", player2_board[:7])
    print("player1:", board[:7])

def is_finalboard(board):
    count1 =0
    count2 =0
    for i in board[:6]:
        if i != 0:
            count1 =-1
            break
    for j in board[7:13]:
        if j != 0:
            count2 = -1
            break
    if (count1 == 0 or count2 ==0):
        return True
    return False

def save_board(board):
    file2 = open(r"board_state.txt","w+")
    file2.write(str(board))
    file2.close()

def load_board():
    file2 = open(r"board_state.txt","r+")
    board =file2.read()
    file2.close()
    return board

"""
board = [5,1,3,2,3,2,3  , 2,2,0,1,3,1,0]
#board = [0,0,0,0,0,1,3  , 0,0,0,0,0,0,10]
print_board(board)
print(is_finalboard(board))
print(play(board, block_no  =5, player=1, mode=1))
board = [0,0,0,0,0,1,14  , 0,0,0,0,0,0,10]
print(calc_score(board))
"""

"""board = [6,1,3,2,3,2,3  , 2,2,0,1,3,1,0]
mode = input("For stealing mode press: 1 else press: 0")

#saving and loading board
save_board(board)
saved_brd= load_board()
print(saved_brd)

while(not is_finalboard(board)):
    block_no=input(" Enter a move:")
    board, player= play(board, int(block_no),0, int(mode))
    print_board(board)
    while (player == 0):
        block_no=input(" Well done play again")
        board, player= play(board, int(block_no),0, int(mode))
        print_board(board)"""
    #alpha beta plays
    #print board again
#calc score
