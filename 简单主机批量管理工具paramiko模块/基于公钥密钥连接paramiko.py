import paramiko

private_key = paramiko.RSAKey.from_private_key_file( '/home/auto/.ssh/id_rsa' )

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
# 连接服务器
ssh.connect( hostname = '192.168.98.128', port = 22, username = 'qkq6988751', key = private_key )

# 执行命令
stdin, stdout, stderr = ssh.exec_command( 'df' )
# 获取命令结果
result = stdout.read()

# 关闭连接
ssh.close()