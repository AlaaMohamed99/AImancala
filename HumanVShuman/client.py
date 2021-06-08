import socket
from sys import path
from typing import NoReturn


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
data=s.recv(1024) #buuuffeerr#
strings=str(data,'utf-8')
num=int(strings)
print(num)
#print(msg.decode("utf-8"))


