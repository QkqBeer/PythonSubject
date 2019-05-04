__author__ = "那位先生Beer"
import socket
import gevent
from gevent import socket,monkey
monkey.patch_all()

def server():
    s=socket.socket()
    s.bind(('localhost',6969))
    s.listen(500)
    while True:
        conn, addr = s.accept()
        gevent.spawn(handle_request,conn)

def handle_request(conn):
    try:
        while True:
            data=conn.recv(1024)
            print("recv:",data)
            conn.send(data)
            if not data:
                conn.shutdown(socket.SHUT_WR)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
if __name__=="__main__":
    server()







