#字典的应用
#  def func(**kwargs):
#     print(kwargs["name"])
# func(name="qkq",age=24,sex="男")

#迭代小尝试
# def cal(n):
#     if n==0 :
#        return 0
#     return  cal(n-1)+n
# print(cal(10))

#文件的字符转python的数据格式 eval（数据）方法
# with open("字符串转数据","r") as f :  #使用这种文件打开方式自动关闭文件
#     data = f.readline( )
# print(data)
# print(eval(data))
# shopping=[]
# shopping=eval(data)
# print(shopping[0][0]+" "+str(shopping [0][1]))


#匿名函数
# cal=lambda x:x*3
# print(cal(3))

#高阶函数：

#a，把函数名当实参传另外一个函数
# def func1():
#     print("func1")
# def func2(f):
#     f()
#     print("func2")
# func2(func1)

#b，返回值中包含函数名
# def func1():
#     return func1
# print(func1())
# #打印func1的首地址

#嵌套函数
# def father():
#     def son():
#         print("in the son")
#     return son
# func=father()
# func()

# 装饰器
# import time
# def timmer(func):
#     def changeFunc():
#         time_start=time.time()
#         func()
#         time_stop=time.time()
#         print("this func have use %s time" %(time_stop-time_start))
#     return changeFunc
#
# @timmer #类似于代码 test=timmer（test） test（）
# def test():
#     time.sleep(3)
#     print("in the test")
# test()


#装饰器,被装饰的函数
# import time
# def timmer(func):
#     def changeFunc():
#         time_start=time.time()
#         res=func() #将返回值记录下来，以及对返回值做操作
#         time_stop=time.time()
#         print("this func have use %s time" %(time_stop-time_start))
#         return res #将返回值返回
#     return changeFunc
# @timmer
# def test():
#     time.sleep(3)
#     print("in the test")
# @timmer
# def test2():
#     time.sleep(1)
#     print("ih the test2")
#     return 1
# test()
# print(test2())


#装饰器，根据不一样的函数来进行不同装饰,给装饰器加参数
# import time
# def timmer(key):
#     def outChangeFunc(func):
#         def changeFunc(*args,**kwargs):#参数
#             if key=="test":
#                 time_start = time.time( )
#                 func(*args,**kwargs)  # 将返回值记录下来，以及对返回值做操作
#                 print(args[0],args[1])
#                 time_stop = time.time( )
#                 print( "this func have use %s time" % (time_stop - time_start) )
#             elif key=="test1":
#                 func()
#                 print("test1 welcome to you")
#         return changeFunc
#     return outChangeFunc
# @timmer("test")
# def test(arg1,arg2):
#     time.sleep(3)
#     print("in the test")
# @timmer("test1")
# def test1():
#     time.sleep(1)
#     print("ih the test1")
# test(1,2)
# test1()

#斐波那契函数
# def fib(max):
#     a,b,n=0,1,1
#     while n<max:
#         print(b)
#         a,b=b,a+b
#         n+=1
# fib(10)