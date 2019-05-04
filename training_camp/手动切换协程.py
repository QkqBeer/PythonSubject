__author__ = "那位先生Beer"
from greenlet import greenlet
def test1():
    print("hello")
    g2.switch()
    print("kai")
    g2.switch()
def test2():
    print("qiu")
    g1.switch()
    print("qiang")

g1=greenlet(test1)
g2=greenlet(test2)
g1.switch()#手动挡切换