__author__ = "那位先生Beer"
import copy
def fatherFunc():
    L = []
    t = 0
    def sonFunc():
        L1 = []
        L1.append('a')
        L1.append('b')
        L = L1
        t = 1
    sonFunc()
    print(L)
    print(t)
fatherFunc()
#这是怎么一回事？？
#总结：在子函数中可以对父函数的变量进行操作，但不能进行赋值操作，赋值操作相当于从新定义了一个新的变量