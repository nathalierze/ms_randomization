#amqps://mebtgqnh:tSpgrFj1GyEh4DghhkHYb-WfjyrtYfdF@stingray.rmq.cloudamqp.com/mebtgqnh

import pika, json

params = pika.URLParameters('amqps://mebtgqnh:tSpgrFj1GyEh4DghhkHYb-WfjyrtYfdF@stingray.rmq.cloudamqp.com/mebtgqnh')


connection = pika.BlockingConnection(params)

channel = connection.channel()


# def publish(method, body):
def publish():
    print("def publish")
    channel.basic_publish(exchange='', routing_key='ortho_queue', body='hallo ich bin der python service')