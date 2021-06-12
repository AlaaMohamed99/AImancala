import socket
from sys import path
from typing import NoReturn
import socket
from AI_final import *
from GAME import *
from  helperfns import * 
import pickle


def convert_string_list(board):
    converted_board = []
    for i in range(1,len(board)-1):
        if (board[i]== ',' or board[i] == ' '):
            continue
        converted_board.append( int(board[i]))
    return converted_board


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
mode=s.recv(1024) #buuuffeerr#
mode=str(mode,'utf-8')


depth = 3
board =[4]*6  + [0] + [4]*6 + [0]
d = Game()
d.draw(board)
a = AI(board)

player =0


while(not is_finalboard(board)):
                  
        if(player == 1):
            bestpath,board,player = a.Minimax_alphabeta( board , depth,alpha_initial , beta_initial,mode ,player )
            d.draw(board)
            print(" Client played:")
            for i in range(1,len(board)+11):
                pass
            s.send(bytes(str( board),"utf-8"))
            for i in range(1,len(board)+11):
                pass
            s.send(bytes(str(player),"utf-8"))
            
        if(player == 0):
            board =s.recv(1024)
            print(board)
            board = convert_string_list(board.decode())
            turn =s.recv(1024)
            player = int(turn.decode()) 
            d.draw(board)
            print(" Server Played")
            print(player)

            
score, winner = calc_score(board)
if winner == 0:
    print("First player (server) won!")
elif winner == 1:
    print("Second player (client) won!")
else:
    print("Draw! no one won!")
  