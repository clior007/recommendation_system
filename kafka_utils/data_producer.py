import csv
from kafka import KafkaProducer


# Kafka broker connection details
producer = KafkaProducer(bootstrap_servers='localhost:9093')

# Open and read the CSV file
with open('data/ml-25m/links.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  next(reader)  # Skip header row (if present)
  for row in reader:
    # Convert row data to a string (or desired format)
    message = ','.join(row)
    producer.send('my_csv_topic', message.encode('utf-8'))

producer.flush()



