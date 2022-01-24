import pika, json, os, django
import schueler.grouping as grouping
import producer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

params = pika.URLParameters('amqps://mebtgqnh:tSpgrFj1GyEh4DghhkHYb-WfjyrtYfdF@stingray.rmq.cloudamqp.com/mebtgqnh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin') 


def callback(ch, method, properties, body):
    print('Received in admin')
    group = grouping.grouping(body)
    producer.publish(group)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()