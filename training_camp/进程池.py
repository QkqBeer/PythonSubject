__author__ = "那位先生Beer"
import os,time
from multiprocessing import Pool
def son_process(num):
    time.sleep(2)
    print("%s:%s"%(num+100,os.getpid()))
    return num

def callback_method(arg):  #进程会有一个返回值给callback回调方法
    print("%s:%s"%(arg+100,os.getpid()))

if __name__=="__main__":
    pool=Pool(processes = 5)#允许进程池同时放入的最大值
    for i in range(10):
        # 串行
        #pool.apply( func = son_process,args=(i,) )
        # 并行
        pool.apply_async(func = son_process,args = (i,),callback = callback_method)
    print("main process end")
    pool.close()
    pool.join()



