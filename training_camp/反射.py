class Person:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print('eat food')


p=Person('qkq')
chooice=input("enter your chooice:")
if hasattr(p,chooice ): #返回TRUE  or FALSE
    getattr(p,chooice)() #返回方法的地址
    setattr(p,'name','gsx')#修改属性p.name='gsx'
    print(p.name)
    delattr(p,'name') #删除p.name属性
    print(p.name)