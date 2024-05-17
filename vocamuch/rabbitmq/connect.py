# amqp://guest:guest@localhost:/5672

import json
import pika


# f = open('./config/config.json')
# config = json.load(f)

rabbitmq = {
        "host": "localhost",
        "username": "guest",
        "password": "guest",
        "port": "5672",
        "queue": "fastq"

    }

class RabbitMQConnect:
    def __init__(self):
        self.queue_name = rabbitmq["queue"]
        self.credentials = pika.PlainCredentials(rabbitmq['username'], rabbitmq['password'])
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbitmq['host'])
            )
        self.channel = self.connection.channel()
        self.publish_queue = self.channel.queue_declare(queue=self.queue_name)
        self.channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
        self.channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback="*******Recieved*********")
        self.response = None
        print('Pika connection initialized')
        self.connection.close
 


# Closing file
# f.close()