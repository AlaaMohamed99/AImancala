import socket
from sys import path
from typing import NoReturn
import socket
from AI_final import *
from GAME1 import *
from  helperfns import * 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
mode=s.recv(1024) #buuuffeerr#
mode=str(mode,'utf-8')
# mode=print(num)
#print(msg.decode("utf-8"))
board =[4]*6  + [0] + [4]*6 + [0]

#print(board)
d = Game()
d.draw(board)


board =s.recv(1024) #buuuffeerr#

while(not is_finalboard(board)):
                  
        while(player == 1):
            bestpath,board,player = a.Minimax_alphabeta( board , depth,alpha_initial , beta_initial ,player )
            clientsocket.send(bytes(str( d.draw(board)),"utf-8"))
            
        while(player == 0):

            

  