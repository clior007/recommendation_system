from utils.config import SingletonConfigLoader
from kafka import KafkaAdminClient, KafkaProducer
from kafka.admin import NewPartitions


class KafkaProducerAdmin:
    def __init__(self) -> None:
        self._config = SingletonConfigLoader()
        self._producers = {}

    def add_producers(self):
        kafka_topics = self._config.get_value(f'servers.kafka.topics')
        
        for topic_name in kafka_topics:
            server = kafka_topics[topic_name]['server']
            port = kafka_topics[topic_name]['port']
            admin_client = KafkaAdminClient(bootstrap_servers=f'{server}:{port}')
            if not topic_name in admin_client.list_topics():
                print (f'Creating topic: {topic_name}')
                num_partitions = kafka_topics[topic_name]['partitions']
                replication_factor = kafka_topics[topic_name]['replication_factor']

                producer = KafkaProducer(bootstrap_servers=f'{server}:{port}')
                producer.send(topic_name, "test".encode('utf-8'))
                self._producers[topic_name] = producer

                topic_partitions = {}
                topic_partitions[topic_name] = NewPartitions(total_count=num_partitions)
                admin_client.create_partitions(topic_partitions)
            
            admin_client.close()

    def close_producers(self):
        for topic in self._producers:
            print(f"Closing producer: {topic}")
            self._producers[topic].flush()
            self._producers[topic].close()

    def delete_topics(self):
        kafka_topics = self._config.get_value(f'servers.kafka.topics')

        for topic_name in kafka_topics:
            server = kafka_topics[topic_name]['server']
            port = kafka_topics[topic_name]['port']
            admin_client = KafkaAdminClient(bootstrap_servers=f'{server}:{port}')
            if topic_name in admin_client.list_topics():
                admin_client.delete_topics([topic_name])

