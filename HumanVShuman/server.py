import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(),1234))
s.listen(5)
while True:
    clientsocket, address =s.accept()
    print(f"connection from {address} has been established")

    value=str(input("enter cup num"))
    clientsocket.send(bytes(str(value),"utf-8"))

    
    #clientsocket.send(value)
    
    





