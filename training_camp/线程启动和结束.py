import threading ,time
time_start=time.time()
def run(n):
    print("task->",n)
    time.sleep(2)
Thread_list=[]
for i in range(50):
    t=threading.Thread(target=run,args=(i,))
    t.start()
    Thread_list.append(t)
for t in Thread_list :
    t.join()#等待线程结束
print("cost time:",time.time()-time_start )