__author__ = "那位先生Beer"
import gevent
def First():
    print("first 1")
    gevent.sleep(2)
    print("first 2")
def Second():
    print("Second 1")
    gevent.sleep(1)
    print("Second 2")
def Third():
    print("Third 1")
    gevent.sleep(0)
    print("Third 2")

gevent.joinall([gevent.spawn(First),gevent.spawn(Second),gevent.spawn(Third)] )
