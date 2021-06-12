from AI_final import *
from GAME import *
from  helperfns import * 

board =[4]*6  + [0] + [4]*6 + [0]
d = Game()
d.draw(board)

load_brd= input("If you want to load the previous board press:1 ,start new game:0")
if int(load_brd) == 1:
    board, mode = load_board()
    player=0
    d.draw(board)
else:

    mode = input("For stealing mode press: 1 else press: 0  ")
    player =int( input("choose 0 if you want to play first else 1 :  "))
# level = int( input("choose difficulty level: "))


if mode==0:
    mode= False
else : mode=True


a = AI(board)
depth = 2
while(not is_finalboard(board)):
    choice = input("If you want to save the game press: 1 else press: 0  ")
    if (int(choice) == 1):
        save_board(board, mode)
        exit()
    else:
        while (player == 0):
            block_no=input(" Enter a move: ")
            board, player= play(board, int(block_no),player, int(mode))       
            d.draw(board)
            if (player==0):
                block_no=input(" play again.....Enter a move: ")
                board, player= play(board, int(block_no),player, int(mode))
                d.draw(board)

        while(player == 1):
            bestpath,board,player = a.Minimax_alphabeta( board , depth,alpha_initial , beta_initial,mode ,player )
            d.draw(board)
            print(bestpath)            

score, winner = calc_score(board)
if winner == 0:
    print("First player won!")
elif winner == 1:
    print("Second player won!")
else:
    print("Draw! no one won!")



