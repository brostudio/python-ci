from pykafka import KafkaClient

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = KafkaClient(hosts="127.0.0.1:9092")
    topic = client.topics['my_favorite_topic']

    with topic.get_sync_producer() as producer:
        for i in range(4):
            producer.produce(b'test message produced')

