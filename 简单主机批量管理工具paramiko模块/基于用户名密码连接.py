import paramiko
#虚拟机ip，端口
transport = paramiko.Transport(('192.168.98.128', 22))
#虚拟机id，密码
transport.connect(username='qkq6988751', password='6988751qkq')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())

transport.close()