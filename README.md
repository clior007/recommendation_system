This is a data science project with the main focus of building a recommendation system for movies.

Enter the kafka docker contianer to control the topics configuration
docker exec -it training-kafka-1 /bin/bash

Now there are few options to query the topics:
1. Create a new topic - kafka-topics.sh --bootstrap-server localhost:9092 --topic movies --create --partitions 3 --replication-factor 1
2. Get list of topics - kafka-topics.sh --bootstrap-server localhost:9093 --list
3. Get description of specific topic - kafka-topics.sh --bootstrap-server localhost:9093 --describe --topic movies
4. Delete a topic - kafka-topics.sh --bootstrap-server localhost:9093 --delete --topic movies
5. Change the number of partitions - kafka-topics.sh --bootstrap-server localhost:9093 --alter --topic movies --partitions 5
