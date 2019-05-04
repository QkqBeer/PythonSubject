__author__ = "那位先生Beer"
from redishelper import RedisHelper
#在指令环境下 public 频道  “消息”
obj = RedisHelper()
obj.public( 'hello' )