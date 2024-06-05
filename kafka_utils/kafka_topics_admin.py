from time import sleep

from utils.config import SingletonConfigLoader
from kafka.admin import KafkaAdminClient, NewTopic


class KafkaTopicsAdmin:
    def __init__(self) -> None:
        self._config = SingletonConfigLoader()
        self._producers = {}
        self._topic_patrtitions = {}

        kafka_servers = self._config.get_value(f'servers.kafka')
        server = kafka_servers['server']
        port = kafka_servers['port']
        self._admin_client = KafkaAdminClient(bootstrap_servers=f'{server}:{port}')

    def add_topics(self):
        kafka_topics = self._config.get_value(f'servers.kafka.topics')

        for topic_name in kafka_topics:
            num_partitions = kafka_topics[topic_name]['partitions']
            self._topic_patrtitions[topic_name] = num_partitions
            if not topic_name in self._admin_client.list_topics():
                print (f'Creating topic: {topic_name}')
                new_topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=1)
                
                try:
                    create_topics_future = self._admin_client.create_topics(new_topics=[new_topic], timeout_ms=60000)
                    sleep(3)

                except Exception as e:
                    print(f"Failed to create topic {topic_name}: {e}")
                
    def get_num_partitions(self, topic_name):
        return self._topic_patrtitions[topic_name]

    def delete_topics(self, topic_name):
        kafka_topics = self._config.get_value(f'servers.kafka.topics')
        for topic_name in kafka_topics:
            if topic_name in self._admin_client.list_topics():
                self._admin_client.delete_topics([topic_name])
                print(f"Deleting topic {topic_name}")
    
    def close(self):
        self._admin_client.close()