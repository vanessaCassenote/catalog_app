# Create : python -m venv nome_venv
# Activate: source nome_venv/bin/activate
# conda create --name nome_env
# conda env list
# conda activate nome_env
# deactivate

# https://dev.to/felipepaz/getting-started-with-rabbitmq-and-python-a-practical-guide-57fi
# The RabbitMQ server will be accessible at localhost:5672, and the management console will be available at http://localhost:15672.

import pika
import os

class RabbitMQ():

    def __init__(self):
        self.user = 'guest'
        self.password = 'guest'
        self.connection = None
        self.channel = None
        
        self.connect()

    def connect(self):
        self.connection = pika.BlockingConnection(pika.URLParameters("amqp://"+self.user+":"+self.password+"@rabbitmq/"))
        self.channel = self.connection.channel()
    
    def publish(self, queue_name, message):
        if not self.channel:
            raise Exception("Connection is not established.")
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.basic_publish(exchange='',
                                   routing_key=queue_name,
                                   body=message,
                                   properties=pika.BasicProperties(
                                       delivery_mode=2,  # make message persistent
                                   ))
        print(f"Sent message to queue {queue_name}: {message}")

    def consume(self, queue_name, callback):
        if not self.channel:
            raise Exception("Connection is not established.")
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()

    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()