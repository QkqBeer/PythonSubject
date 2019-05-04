#新的类创建方法
def func(self):
    print("hello qkq")
Foo=type('Foo',(),{'talk':func})
   #Foo=type（’Foo',(父类)，{新的方法名：方法地址}）
f=Foo()
f.talk()
