__author__ = "那位先生Beer"
import pika
import os
import json
credentials = pika.PlainCredentials( 'qkq', 'qkq6988751' )
connection = pika.BlockingConnection( pika.ConnectionParameters(
         '192.168.98.128', 5672 ,'/',credentials) )
channel = connection.channel()
channel.queue_declare( queue = 'rpc_queue' ) #接收消息的队列

def cmd( ask ):
    print(ask)
    cmd_str=os.popen(ask,"r",1024).read()
    return json.dumps(cmd_str).encode('utf-8')

def on_request( ch, method, props, body ):
    print( "$" % body )
    response = cmd( json.loads(body.decode()) )
    ch.basic_publish( exchange = '',
                      routing_key =props.reply_to,
                      body =  response )
    print(props.reply_to)
    ch.basic_ack( delivery_tag = method.delivery_tag )


channel.basic_qos( prefetch_count = 1 )
channel.basic_consume( on_request, queue = 'rpc_queue' )

print( "RPC requests" )
channel.start_consuming()