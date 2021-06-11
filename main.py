from AI_final import *
from GAME import *
from  helperfns import * 

board =[4]*6  + [0] + [4]*6 + [0]
d = Game()
d.draw(board)

mode = input("For stealing mode press: 1 else press: 0  ")
player =int( input("choose 0 if you want to play first else 1 :  "))
level = int( input("choose difficulty level: "))
a = AI(board)
depth = 3
while(not is_finalboard(board)):



    while (player == 0):
        block_no=input(" Enter a move: ")
        board, player= play(board, int(block_no),player, int(mode))       
        d.draw(board)
        block_no=input(" Well done play again")
        board, player= play(board, int(block_no),0, int(mode))
        d.draw(board)

    while(player == 1):
        bestpath,board,player = a.Minimax_alphabeta( board , depth,alpha_initial , beta_initial ,player )
        d.draw(board)
            
            




