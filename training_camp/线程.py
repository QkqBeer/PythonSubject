import threading,time
def run(name):
    print("task",name)
    time.sleep(2)
t1=threading.Thread (target=run,args=("task1",))#加逗号很关键，否则传入一个元祖
t2=threading.Thread (target=run,args=("task2",))
t1.start()
t2.start()
#对照两种调用方法的差距
# run("task1")
# run("task2")