import socket
import sys
import time

s=socket.socket()
host=input(str("please enter host name:"))
port=1814
try:
    s.connect((host,port))
    print("connected to server")
except:
    print("Connection to server is failed:(")
while 1:
    incoming_message=s.recv(1024)
    incoming_message=incoming_message.decode()
    print("Server:>>",incoming_message)
    message=input(str("You:>>"))
    message=message.encode()
    s.send(message)
    