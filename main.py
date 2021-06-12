from AI_final import *
from GAME import *
from  helperfns import * 

board =[4]*6  + [0] + [4]*6 + [0]
d = Game()
d.draw(board)

load_brd= input("If you want to load the previous board press:1 ,start new game:0 ")
depth_level= int(input("choose difficulty level:\n" +
              '1: easy\n' +'2: meduim\n' +'3:hard\n' ))
if int(load_brd) == 1:
    board, mode = load_board()
    player=0
    d.draw(board)
else:

    mode = input("For stealing mode press: 1 else press: 0  ")
    player =int( input("choose 0 if you want to play first else 1 :  "))
# level = int( input("choose difficulty level: "))

if depth_level == 1:
        depth = 3
elif  depth_level == 1:
        depth = 5
elif  depth_level == 1:
        depth = 8
else: depth = 3
        
        
        
        
if mode==0:
    mode= False
else : mode=True


a = AI(board)
# depth = 2
while(not is_finalboard(board)):
    choice = input("If you want to save the game press: 1 else press: 0   ")
    if (int(choice) == 1):
        save_board(board, mode)
        exit()
    else:
        while (player == 0 and not is_finalboard(board)):
            block_no=input(" Enter a move: ")
            board, player= play(board, int(block_no),player, int(mode))       
            d.draw(board)
            if (player==0):
                block_no=input(" play again.....Enter a move: ")
                board, player= play(board, int(block_no),player, int(mode))
                d.draw(board)

        while(player == 1 and not is_finalboard(board)):
            bestpath,board,player = a.Minimax_alphabeta( board , depth,alpha_initial , beta_initial,mode ,player )
            d.draw(board)
            # print('bestpath ' + str(bestpath))            

score, winner = calc_score(board)
if winner == 0:
    print("You won!")
elif winner == 1:
    print("AI won!")
else:
    print("Draw! no one won!")


input("press close to exit") 
