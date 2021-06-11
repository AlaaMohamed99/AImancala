import socket
from AI_final import *
from GAME1 import *
from  helperfns import * 

board =[4]*6  + [0] + [4]*6 + [0]

#print(board)
d = Game()
d.draw(board)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(),1234))
s.listen(5)
while True:
    clientsocket, address =s.accept()
    #print(f"connection from {address} has been established")
  
    
    mode = str(input("For stealing mode press: 1 else press: 0  "))
    # player =str( input("choose 0 if you want to play first else 1 :  "))
    #level = str( input("choose difficulty level: "))
    a = AI(board)
    depth = 3
    clientsocket.send(bytes(str(mode),"utf-8"))
    # clientsocket.send(bytes(str(player),"utf-8"))
    player = 0
    #value=str(input("enter cup num"))
    while(not is_finalboard(board)):


            while(player == 0):
                bestpath,board,player = a.Minimax_alphabeta_client( board , depth,alpha_initial , beta_initial ,player )
                d.draw(board)   
                # clientsocket.send(bytes(str( d.draw(board)),"utf-8"))
                clientsocket.send(bytes(str((board)),"utf-8"))
    #clientsocket.send(value)

    
    
                
            
    
    #clientsocket.send(bytes(str(level),"utf-8"))


    
    
    





