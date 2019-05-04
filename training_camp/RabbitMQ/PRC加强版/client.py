__author__ = "那位先生Beer"
import pika
import uuid
import json
import threading
#输入cmd指令，例如dir，ipconfig

class FibonacciRpcClient( object ):
    def __init__( self ):
        credentials = pika.PlainCredentials( 'qkq', 'qkq6988751' )
        self.connection = pika.BlockingConnection( pika.ConnectionParameters(
         '192.168.98.128', 5672 ,'/',credentials) )
        self.channel = self.connection.channel()

def call(fibonacci_rpc ,ask ,id ):
    result = fibonacci_rpc.channel.queue_declare( exclusive = True )  # 队列持久化  返回队列
    fibonacci_rpc.callback_queue = result.method.queue  # 队列名字
    listID.append(fibonacci_rpc.callback_queue)
    fibonacci_rpc.channel.basic_publish( exchange = '',
                                routing_key = 'rpc_queue',
                                properties = pika.BasicProperties(
                                    reply_to = fibonacci_rpc.callback_queue,  # 发送一个队列名，指定发送方发送到该队列中
                                ),
                                body = json.dumps( ask ).encode( "utf-8" ) )
def on_response( ch, method, properties, body ):
    if json.loads(body.decode())=='':
        print("输入命令不正确")
    else:
        print(json.loads(body.decode()))

def recvmessage(fibonacci_rpc,id):
    threadlist[int( taskID ) - 1].join()
    fibonacci_rpc.channel.basic_consume(on_response,  # 回调方法，只要收到消息就调用
                                no_ack = True,
                                queue = id)
    #fibonacci_rpc.channel.start_consuming()
    fibonacci_rpc.connection.process_data_events()
    #这个很好用哦，上面是阻塞的，这个是非阻塞版的self.connection.consume方法，不停地检测是否消息接受

fibonacci_rpc = FibonacciRpcClient()
threadlist=[]
listID=[]
while True:
    ask = input( ">>" )
    if ask=="get":
        taskID=input("ID:")
        recvmessage(fibonacci_rpc,listID[int(taskID)-1])
        #调用接收消息，并且结束线程
    else:
        t=threading.Thread(target = call,args = (fibonacci_rpc,ask,len(threadlist),))
        t.start()
        threadlist.append(t)
        print("taskID:",len(threadlist))
        #添加新的线程声明新的队列
