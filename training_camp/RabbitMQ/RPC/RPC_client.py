__author__ = "那位先生Beer"
import pika
import uuid
import json
#输入cmd指令，例如dir，ipconfig

class FibonacciRpcClient( object ):
    def __init__( self ):
        credentials = pika.PlainCredentials( 'qkq', 'qkq6988751' )
        self.connection = pika.BlockingConnection( pika.ConnectionParameters(
         '192.168.98.128', 5672 ,'/',credentials) )
        self.channel = self.connection.channel()

        result = self.channel.queue_declare( exclusive = True ) #队列持久化  返回队列
        self.callback_queue = result.method.queue #队列名字

        self.channel.basic_consume( self.on_response, #回调方法，只要收到消息就调用
                                    no_ack = True,
                                    queue = self.callback_queue )

    def on_response( self, ch, method, props, body ):
        if self.corr_id == props.correlation_id: #判断返回的ID是否和发送ID一致
            self.response = body


    def call( self, ask ):
        self.response = None #声明返回消息
        self.corr_id = str( uuid.uuid4() ) #声明一个随机ID
        self.channel.basic_publish( exchange = '',
                                    routing_key = 'rpc_queue',
                                    properties = pika.BasicProperties(
                                        reply_to = self.callback_queue, #发送一个队列名，指定发送方发送到该队列中
                                        correlation_id = self.corr_id,
                                    ),
                                    body = json.dumps(ask).encode("utf-8"))
        while self.response is None:
            self.connection.process_data_events()  #非阻塞版的self.connection.consume方法，不停地检测是否消息接受
        return  self.response


fibonacci_rpc = FibonacciRpcClient()

while True:
    ask = input( ">>" )
    result=fibonacci_rpc.call( ask )
    print(json.loads(result.decode()))




