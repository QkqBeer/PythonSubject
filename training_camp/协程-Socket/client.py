__author__ = "那位先生Beer"
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',6969))
while True:
    data=bytes(input(">>:"),encoding="utf8")
    s.send(data)
    datarecv=s.recv(1024)
    print("recv:",repr(datarecv))
s.close()
