
import socket
import os,time
server=socket.socket()
server.bind(('localhost',6969))#绑定要监听的端口
server.listen()#监听
while True:
    conn,addr = server.accept()
    # 等电话打进来,conn就是客户端链接过来而在服务器上为其而生成的一个实例
    print("new conn", addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("connection lost........")
            break
        print("执行指令")
        cmd_res=os.popen(data.decode()).read() #接受字符串，执行结果也是字符串
        print("before send",len(cmd_res))
        if len(cmd_res)==0:
            cmd_res="cmd has no output..."
        conn.send(str(len(cmd_res.encode("utf-8"))).encode("utf-8")) #先发大小给客户端
        time.sleep(0.5) #因为缓冲区数据容易黏到一块，返回去的len(cmd_res）会不是也一个整数
        conn.send(cmd_res.encode("utf-8"))
        print ("send done")
server.close()


