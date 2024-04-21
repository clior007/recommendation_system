from utils.config import SingletonConfigLoader
from kafka_utils.kafka_admin import KafkaProducerAdmin

CONFIG_PATH = "utils/config.yaml"

def main():
    print("Hello, recommendation system")

    config_loader = SingletonConfigLoader(CONFIG_PATH)
    csv_data_sources = config_loader.get_value('data_sources.csv')

    kafka_producer_admin = KafkaProducerAdmin()
    kafka_producer_admin.add_producers()

    kafka_producer_admin.close_producers()

    kafka_producer_admin.delete_topics()

    for csv_data_source in csv_data_sources:
        print(csv_data_source)


if __name__ == "__main__":
    main()