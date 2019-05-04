__author__ = "那位先生Beer"
from redishelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:#不停地接收消息
    msg = redis_sub.parse_response()#这才是真正的接收消息
    print(msg)
