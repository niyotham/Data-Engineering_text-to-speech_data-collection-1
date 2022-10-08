from kafka import KafkaConsumer
import json
import msgpack as pk


topic_name = 'g1-raw-text-data-topic-dev'
bootstrap_server = ['localhost:9092']
aws_instance_bootstrap_servers = ['b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092',
                                  'b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092']
# To consume latest messages and auto-commit offsets
# consumer = KafkaConsumer('g1-voices-test-topic',
#                        group_id='my-group-g1',
#                       bootstrap_servers=aws_instance_bootstrap_servers)

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(topic_name,
                         group_id='my-group',
                         bootstrap_servers=aws_instance_bootstrap_servers)

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))

# consume earliest available messages, don't commit offsets
KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# consume json messages
KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))

# consume msgpack
KafkaConsumer(value_deserializer=msgpack.unpackb)

# StopIteration if no message after 1sec
KafkaConsumer(consumer_timeout_ms=1000)

# Subscribe to a regex topic pattern
consumer = KafkaConsumer()
consumer.subscribe(pattern='^awesome.*')

# Use multiple consumers in parallel w/ 0.9 kafka brokers
# typically you would run each on a different server / process / CPU
consumer1 = KafkaConsumer(topic_name,
                          group_id='my-group',
                          bootstrap_servers=aws_instance_bootstrap_servers)
"""
consumer2 = KafkaConsumer('my-topic',
                          group_id='my-group',
                          bootstrap_servers='my.server.com')
"""
