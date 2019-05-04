__author__ = "那位先生Beer"
import os
cmd_res=os.popen("ipconfig").read() #接受字符串，执行结果也是字符串
print("before send",cmd_res)
