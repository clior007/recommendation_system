
import csv
from utils.config import SingletonConfigLoader


class CSVReadersAdmin:
    def __init__(self) -> None:
        self._config = SingletonConfigLoader()
        self._readers = {}

    def add_readers(self):
        data_sources_topics = self._config.get_value('data_sources.topics')
        for csv_data_topic in data_sources_topics:
            csvfile = open(data_sources_topics[csv_data_topic]['path'], 'r')
            reader = csv.reader(csvfile)
            self._readers[csv_data_topic] = reader

    def get_readers(self):
        return self._readers

    def close_readers(self):
        for reader in self._readers:
            print(f"Closing reader: {reader}")
            self._readers[reader].close()
    
    def read(self, topic_name):
        reader = self._readers[topic_name]
        return next(reader)
