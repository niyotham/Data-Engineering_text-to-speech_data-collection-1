from kafka import KafkaProducer
from kafka.errors import KafkaError
import msgpack as pk
# import json


aws_instance_bootstrap_servers = ['b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092',
                                  'b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092']

producer = KafkaProducer(bootstrap_servers=aws_instance_bootstrap_servers)

# Asynchronous by default
future = producer.send('g1-voices-test-topic', b'raw_bytes')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

# Successful result returns assigned partition and offset
print(record_metadata.topic)
print(record_metadata.partition)
print(record_metadata.offset)

# produce keyed messages to enable hashed partitioning
producer.send('g1-voices-test-topic', key=b'foo', value=b'bar')

# encode objects via msgpack
producer = KafkaProducer(value_serializer=pk.dumps)
producer.send('msgpack-topic', {'key': 'value'})

# produce json messages
# TODO: the line below was not commented
# TODO: https://bobbyhadz.com/blog/python-typeerror-object-of-type-bytes-is-not-json-serializable#:~:text=The%20Python%20%22TypeError%3A%20Object%20of,string%20before%20serializing%20to%20JSON.
# producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).decode('utf-8').encode('utf-8'))
producer.send('json-topic', {'key': 'value'})

# produce asynchronously
for _ in range(100):
    producer.send('g1-voices-test-topic', b'msg')


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)


def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception


# produce asynchronously with callbacks
producer.send('g1-voices-test-topic',
              b'raw_bytes').add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5)
