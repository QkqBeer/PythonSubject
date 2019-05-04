__author__ = "那位先生Beer"
import redis

pool = redis.ConnectionPool( host = '192.168.98.128', port = 6379 )

r = redis.Redis( connection_pool = pool )

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline( transaction = True )

pipe.set( 'name', 'alex' )
pipe.set( 'role', 'sb' )

pipe.execute()