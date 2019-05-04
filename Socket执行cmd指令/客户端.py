import socket
client=socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))
while True:
    cmd=input(">>:").strip()
    if len(cmd)==0:continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size=client.recv(1024) #接受命令的结果长度
    print("命令结果大小：",cmd_res_size )
    received_size=0
    received_data=b''
    while received_size < int(cmd_res_size.decode()):
        data =client.recv(1024)
        received_size +=len(data) #每次收到的有可能小于1024，所以必须判断
        received_data +=data
    else:
        print("cmd res receive done...",received_size )
        print(received_data.decode())

client.close()




