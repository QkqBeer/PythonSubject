__author__ = "那位先生Beer"
import redis

#为了方便将两个方法集成到一个类里面（收发消息）
class RedisHelper:

    def __init__(self):#初始化方法
        self.__conn = redis.Redis(host='192.168.98.128') #连接这台机器
        self.chan_sub = 'fm104.5'#发
        self.chan_pub = 'fm104.5'#收

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg) #发消息
        return True

    def subscribe(self):
        pub = self.__conn.pubsub() #打开收音机
        pub.subscribe(self.chan_sub)#连接频道
        pub.parse_response()#准备接受
        return pub