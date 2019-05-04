__author__ = "那位先生Beer"
import pika

credentials = pika.PlainCredentials( 'qkq', 'qkq6988751' )

connection = pika.BlockingConnection( pika.ConnectionParameters(
    '192.168.98.128', 5672, '/', credentials ) )
channel = connection.channel()

channel.queue_declare( queue = 'hello3'
                       ,durable = True
                       )
#queue = 'hello'队列名字,durable = True队列持久化，但是不能使消息持久化
channel.basic_publish( exchange = '',
                       #exchange的类型决定了发送消息的类型，决定了哪些queue符合接受类型
                       routing_key = 'hello3',
                       #hello2 不是队列持久化，更改时需注意
                       body = 'Hello World!',
                       properties = pika.BasicProperties(
                           delivery_mode = 2  #使消息持久化
                       )
                       )
print("[x] Sent 'Hello World!'")
connection.close()