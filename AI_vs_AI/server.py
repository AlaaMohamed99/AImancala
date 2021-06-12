import socket
from AI_final import *
from GAME import *
from  helperfns import * 

def convert_string_list(board):
    converted_board = []
    for i in range(1,len(board)-1):
        if (board[i]== ',' or board[i] == ' '):
            continue
        converted_board.append( int(board[i]))
    return converted_board


board =[4]*6  + [0] + [4]*6 + [0]
d = Game()
d.draw(board)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(),1234))
s.listen(5)
clientsocket, address =s.accept()
print(f"connection from {address} has been established")



mode = str(input("For stealing mode press: 1 else press: 0  "))
a = AI(board)
depth = 3
clientsocket.send(bytes(str(mode),"utf-8"))

player = 0

while(not is_finalboard(board)):

          if(player == 0):
                bestpath,board,player = a.Minimax_alphabeta_client( board , depth,alpha_initial , beta_initial,mode ,player )
                d.draw(board) 
                #print(" Server Played")
                for i in range(1,len(board)+11):
                    pass
                clientsocket.send(bytes(str(board),"utf-8"))
                for i in range(1,len(board)+11):
                    pass
                clientsocket.send(bytes(str(player),"utf-8"))

            
          if(player == 1):
            board =clientsocket.recv(1024)
            board = convert_string_list(board.decode())
            turn =clientsocket.recv(1024)
            player = int(turn.decode())
            d.draw(board)
            print(" Client played:")

score, winner = calc_score(board)
if winner == 0:
    print("First player (server) won!")
elif winner == 1:
    print("Second player (client) won!")
else:
    print("Draw! no one won!")
    #            clientsocket.send(bytes(str((board)),"utf-8"))
                
            
    
    #clientsocket.send(bytes(str(level),"utf-8"))


    
    
    





