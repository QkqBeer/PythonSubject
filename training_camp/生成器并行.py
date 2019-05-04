def consumer(name):
    print("%s 准备吃包子了"%name)
    while True:
        baozi = yield
        print("[%s] 吃了[%s] 包子"%(name, baozi))
# c=consumer("qkq")
# c.__next__()
# b="茶树菇"
# c.send(b)
def producer():
    c=consumer("qkq")#将函数consumer（）函数转换成生成器
    c1=consumer("hyk")
    c.__next__ () #执行yield前的代码，唤醒yield
    c1.__next__()
    print("准备蒸包子")
    for i in range(10):
        c.send(i)#唤醒yield，并且可以传值给yield
        c1.send(i)
producer()

