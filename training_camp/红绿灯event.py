import threading
import time


event=threading.Event()

def lighter():
    count=0
    while True:
        if count>=0 and count<5 : #绿灯
            event.set()  #设置标志位
            print("green")
        elif count<10 and count>=5: #红灯
            event.clear()#清空标志位
            print("red")
        else:
            count=0
        count+=1
        time.sleep(1)
def Car(name):
    while True:
        if event.is_set(): #判断是否存在标志位
            time.sleep(1)
            print(" [%s]running" %name)
        else:
            print("[%s] waiting" % name)
            event.wait() #如果存在标志位不执行wait方法，如果没有则执行
            print("等待结束，开始运行")



light=threading.Thread (target=lighter,)
light.start()
car=threading.Thread (target=Car,args=("tesla",))
car.start()