class Foo(object):
    def __init__(self,name):
        print("in the Foo__init")
        self.name=name
    def __new__(cls, *args, **kwargs):#是重写object父类中的new方法
        print("in the Foo__new")
        return object.__new__(cls)
    #new 方法是用来创建实例的，return语句只是来继承父类的new方法，可以在new方法中定制自己的实例对象
f=Foo("qkq")
