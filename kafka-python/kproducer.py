
import datetime
import json

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9093')


def sendMessageToKafkaByProducer(usr,msg):
    print("her*****e")
    the_dt = str(datetime.datetime.now(datetime.UTC))
    user = usr
    word = msg
    sendObj = {
        "user": user,
        "date": the_dt,
        "word": word,
    }
    try:
        producer.send(topic="KafkaExplored", value=json.dumps(sendObj).encode('utf-8'))
        producer.close()
    except Exception as ex:
        print(ex)


sendMessageToKafkaByProducer("root", "Big")
# try:
#     for _ in range(10):
#         the_dt = str(datetime.datetime.now(datetime.UTC))
#         val = f"Count: {_} at {the_dt}".encode(encoding='utf8')
#         producer.send(topic="KafkaExplored", value=val)
#     producer.close()

# except Exception as ex:
#     print(ex)