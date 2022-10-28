from pykafka import KafkaClient


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = KafkaClient(hosts="127.0.0.1:9092")
    topic = client.topics['my_favorite_topic']

    consumer = topic.get_simple_consumer()
    for message in consumer:
        if message is not None:
            print(message.offset, message.value)
