# kconsumer.py

from kafka import KafkaConsumer

consumer = KafkaConsumer('KafkaExplored', bootstrap_servers='localhost:9093')


print('****consumer-',consumer)
print('*************')
for msg in consumer:
    topic = msg[0]
    value = msg[6]
    print(msg)
    print(f"{topic}:{value.decode()}")