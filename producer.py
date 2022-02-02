# #amqps://mebtgqnh:tSpgrFj1GyEh4DghhkHYb-WfjyrtYfdF@stingray.rmq.cloudamqp.com/mebtgqnh

# import pika, json

# # def publish(body):
# #     params = pika.URLParameters('amqps://mebtgqnh:tSpgrFj1GyEh4DghhkHYb-WfjyrtYfdF@stingray.rmq.cloudamqp.com/mebtgqnh')
# #     connection = pika.BlockingConnection(params)
# #     channel = connection.channel()
# #     channel.queue_declare(queue='ortho_queue')

# #     channel.basic_publish(exchange='',
# #                       routing_key='ortho_queue',
# #                       body='Hello World!')
# #     print(" [x] Sent 'Hello World!'")

# #     connection.close()

# # def publish(body):
# #     print("test")


# params = pika.URLParameters('amqps://mebtgqnh:tSpgrFj1GyEh4DghhkHYb-WfjyrtYfdF@stingray.rmq.cloudamqp.com/mebtgqnh')
# connection = pika.BlockingConnection(params)

# channel = connection.channel()

# def publish(body):
#     print("def publish2")
#     print(body)
#     test = 'thistest'
#     channel.basic_publish(exchange='', routing_key='ortho_queue', body=test, properties=pika.BasicProperties(expiration='1000'))