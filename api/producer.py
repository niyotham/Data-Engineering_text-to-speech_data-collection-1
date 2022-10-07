from kafka import KafkaProducer

def produce(topic,message,bootstrap_servers=['b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092',
    'b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092']):
    producer = KafkaProducer(bootstrap_servers)
    for i in ['k','f','l']:
        msg = bytes(f"{message}", encoding='utf-8')
        producer.send(topic, msg)
        producer.flush()
    print("Produced!")