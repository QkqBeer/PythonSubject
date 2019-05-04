__author__ = "那位先生Beer"
import pika

credentials = pika.PlainCredentials( 'qkq', 'qkq6988751' ) #设置的登录名和密码（与Linux的登录名不一样）

connection = pika.BlockingConnection( pika.ConnectionParameters(
    '192.168.98.128', 5672, '/', credentials ) )
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare( queue = 'hello3',durable = True)#必须接收和发送方对队列的要求是一致的
def callback( ch, method, properties, body ): #body代表消息内容
    print( " [x] Received %r" % body )
# channel.basic_qos(prefetch_count = 1) #实现根据处理进度分配给每个消费者只拥有一个消息或任务
channel.basic_consume( callback,
                       queue = 'hello3',
                       no_ack = True  #不需确认
                     )
print( ' [*] Waiting for messages. To exit press CTRL+C' )
channel.start_consuming()