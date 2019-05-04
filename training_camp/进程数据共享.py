__author__ = "那位先生Beer"
from multiprocessing import Process,Manager
import os
def son_process(dict,list):
    dict["name"]='qkq'
    dict["age"]=25
    dict["sex"]='male'
    list.append( os.getpid())


if __name__=="__main__":
    with Manager() as  manager:
        dict=manager.dict()
        list=manager.list()
        p_list=[]
        for i in range(10):
            p=Process(target = son_process,args=(dict,list,))
            p_list.append(p)
            p.start()
        for i in p_list:
            i.join()

        print(dict)
        print(list)
