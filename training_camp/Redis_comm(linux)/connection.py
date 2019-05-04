__author__ = "那位先生Beer"
import redis

r = redis.Redis( host = '192.168.98.128', port = 6379 )
r.set( 'foo', 'Bar' )
print (r.get( 'foo' ))