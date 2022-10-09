import json
from kafka import KafkaConsumer

def consume(topic, group, time_out=305000, bootstrap_servers=[
                                'b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092',
                                'b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092'
                            ]):
    consumer = KafkaConsumer(topic,
                            bootstrap_servers=bootstrap_servers,
                            auto_offset_reset='latest',
                            enable_auto_commit=True,
                            group_id=group,
                            consumer_timeout_ms=time_out)
    messages=[]
    for msg in consumer:

        data=json.loads(msg.value.decode('utf8'))

        messages.append(data)

    return json.dumps(messages)
        # print(data)
                
        # msg is a tuple
        # (topic='g1-test-topic',
        # partition=0, 
        # offset=403, 
        # timestamp=1664982573369, 
        # timestamp_type=0, 
        # key=None, 
        # value=b'some_message_bytes', 
        # headers=[], checksum=None, 
        # serialized_key_size=-1, 
        # serialized_value_size=18, 
        # serialized_header_size=-1)