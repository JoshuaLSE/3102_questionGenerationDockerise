from pipelines import pipeline
import pika

# !/usr/bin/env python
import pika
import time


class QuestionGen:
    def __init__(self):
        # Define Pipeline
        self.nlp = pipeline("e2e-qg")

    def processText(self, text):
        """
        Process and print the stored text
        """
        print(self.nlp(text))


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
QG = QuestionGen()
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    QG.processText(body.decode())
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
