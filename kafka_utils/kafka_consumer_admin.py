import random

from utils.config import SingletonConfigLoader
from kafka import KafkaConsumer
from kafka.structs import TopicPartition


class KafkaConsumerAdmin:
    def __init__(self) -> None:
        self._topic_patrtitions = {}
        self._config = SingletonConfigLoader()
        kafka_servers = self._config.get_value(f'servers.kafka')
        server = kafka_servers['server']
        port = kafka_servers['port']
        self._consumer = KafkaConsumer(bootstrap_servers=f'{server}:{port}', auto_offset_reset='earliest')
        
    def receive_message(self, kafka_topics_admin, topic):
        partition_number = random.randint(0, kafka_topics_admin.get_num_partitions(topic) - 1)
        self._consumer.assign([TopicPartition(topic, partition_number)])
        for message in self._consumer:
            print(f"Receiving message from topic {topic} partition {partition_number}: {message}")
    
    def close_consumer(self):
        self.close_consumer()
