import random

from utils.config import SingletonConfigLoader
from kafka import KafkaProducer


class KafkaProducerAdmin:
    def __init__(self) -> None:
        self._topic_patrtitions = {}
        self._config = SingletonConfigLoader()
        kafka_servers = self._config.get_value(f'servers.kafka')
        server = kafka_servers['server']
        port = kafka_servers['port']
        self._producer = KafkaProducer(bootstrap_servers=f'{server}:{port}')
        
    def send_message(self, kafka_topics_admin, topic, message):
        partition_number = random.randint(0, kafka_topics_admin.get_num_partitions(topic) - 1)
        self._producer.send(topic, value=message.encode('utf-8'), partition=partition_number)
        print(f"Sent message to topic {topic} partition {partition_number}: {message}")
    
    def close_producer(self):
        self._producer.flush()
        self._producer.close()

    

