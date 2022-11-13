from pipelines import pipeline
import pika
import json
from sqlalchemy_orm import SQLStuff


class QuestionGen:
    def __init__(self):
        # Define Pipeline
        self.nlp = pipeline("e2e-qg")

    def processText(self, text):
        """
        Process and print the stored text
        """
        return self.nlp(text)[0]


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

# Initiate Question Generation Pipeline
QG = QuestionGen()
# Initiate SQLConnector
control = SQLStuff("root", "root", "localhost", "3306", "02db")


def callback(ch, method, properties, body):
    result = QG.processText(body.decode())
    control.insert(name=result, color=result)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
