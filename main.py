import csv

from utils.config import SingletonConfigLoader
from kafka_utils.kafka_producer_admin import KafkaProducerAdmin
from kafka_utils.kafka_consumer_admin import KafkaConsumerAdmin
from kafka_utils.kafka_topics_admin import KafkaTopicsAdmin
from data_providers.csv.csv_admin import CSVReadersAdmin

CONFIG_PATH = "utils/config.yaml"

def main():
    print("Hello, recommendation system")

    config_loader = SingletonConfigLoader(CONFIG_PATH)
    kafka_topics_admin = KafkaTopicsAdmin()
    kafka_topics_admin.add_topics()
    
    csv_readaers_admin = CSVReadersAdmin()
    csv_readaers_admin.add_readers()
    csv_readers = csv_readaers_admin.get_readers()

    kafka_producer_admin = KafkaProducerAdmin()
    kafka_consumer_admin = KafkaConsumerAdmin()
    for topic in csv_readers:
        reader = csv_readers[topic]
        # todo add multithreading here - each reader should be a separate thread
        i = 0
        for row in reader:
            if i >= 10:
                break
            message = ','.join(row)
            kafka_producer_admin.send_message(kafka_topics_admin, topic, message)
            i += 1

        kafka_consumer_admin.receive_message(kafka_topics_admin, topic)

    print("Done")
        
        


    







    #csv_data_sources = config_loader.get_value('data_sources.topics')
    #for csv_data_source in csv_data_sources:
    #    print(csv_data_source)
    #    with open(csv_data_sources[csv_data_source]['path'], 'r') as csvfile:
    #        reader = csv.reader(csvfile)
    #        next(reader)  # Skip header row (if present)
    #        for row in reader:
    #            # Convert row data to a string (or desired format)
    #            message = ','.join(row)
    #            producer.send('my_csv_topic', message.encode('utf-8'))
#
    #kafka_producer_admin.close_producers()
#
    #kafka_producer_admin.delete_topics()

        
    



if __name__ == "__main__":
    main()