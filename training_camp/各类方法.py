#静态方法





#属性方法
class P:
    def __init__(self,name):
        self.name=name

    @property
    def eat(self):
        print("%s eat something %s"%(self.name,self.__food))

    @eat.setter
    def Eat(self,food):# 此名随意
        print("set to food:" ,food)
        self.__food=food
    #call方法 __init__() 构造方法是由创建对象出发的，即：对象=类（）。
    # 而对于__call__()方法是由对象（）所触发，即：对象（）或类（）（）
    def __call__(self):
        print("running call")
person=P("qwer")
person.Eat="chocolate"
#属性方法，将一个方法变成一个静态属性
person.eat

person()