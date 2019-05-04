# 装饰器
# import time
# def timmer(func):
#     #重写函数功能
#     def changeFunc():
#         time_start=time.time()
#         func()
#         time_stop=time.time()
#         print("this func have use %s time" %(time_stop-time_start))
#     return changeFunc
#
# @timmer #类似于代码 test1=timmer（test1） test1（）给函数重新附上新的首地址
# def test1():
#     time.sleep(3)
#     print("in the test")
# test1()

def InitialUp(func):
    def inner(*args, **kwargs):
        t = func(args[0])
        s = t[0].upper() + t[1:]
        return s
    return inner

@InitialUp
def beizhuangshi(zifuchuan):
    return zifuchuan

print(beizhuangshi('qkqqkqq'))
