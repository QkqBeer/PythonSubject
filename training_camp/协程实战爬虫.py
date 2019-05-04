__author__ = "那位先生Beer"
import gevent
from urllib import request
import time
from gevent import monkey

monkey.patch_all()#把当前程序中所有的io操作都打上标记,不然gevent不能进行异步操作
def f(url):
    print("Get： %s"%url)
    resp=request.urlopen(url)
    data=resp.read()
    print("%s bytes received from %s"%(len(data),url))

time_strat=time.time()
gevent.joinall([gevent.spawn(f,'https://www.baidu.com/'),
                gevent.spawn(f,'http://xueshu.baidu.com/'),
                gevent.spawn(f,'https://github.com/')])
print("spend time :",(time.time()-time_strat))