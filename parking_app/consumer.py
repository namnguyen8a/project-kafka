from kafka import KafkaConsumer

consumer = KafkaConsumer('vehicles', bootstrap_servers='localhost:29092')

print("Gonna start listening")

for message in consumer:
    print("Here is all vehicles")
    print (message)