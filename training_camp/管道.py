__author__ = "那位先生Beer"
#类似于socket
from multiprocessing import Process,Pipe

def Lift_entrance(lift):
    lift.send("hello")
    print(lift.recv())
    lift.close()

if __name__=="__main__":
   right,lift=Pipe()
   p_Lift=Process(target = Lift_entrance,args=(lift,))
   p_Lift.start()
   print(right.recv())
   right.send("what are you doing?")



