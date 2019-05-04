 # '''shelve模块是一个简单的key，value。将内存数据通过文件持久化的模块，
 #    可以持久化任何pickle可支持的python数据格式'''

import shelve
from core import SchoolMember
def readFile(fileName):
    list=[]
    db=shelve.open(fileName)
    for key in db:
        list.append(db[key])
    db.close()
    return list
def writeFile(fileName,data):
    db=shelve.open(fileName)
    for i in data:
        db[i.name]=i
    db.close()

