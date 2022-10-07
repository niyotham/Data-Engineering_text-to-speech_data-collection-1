import pandas as pd
import json
from kafka import KafkaProducer


def produce_the_message():


    raw_data_ = pd.read_csv('../data/raw_data.csv')
    print(raw_data_.shape)

    raw_data = raw_data_.iloc[0:3, ]
    raw_data = raw_data.to_dict()

    print('publishing raw message . . .')
    # raw_data = ti.xcom_pull(key='raw_data_from_csv', task_ids='raw_data_read')
    
    # TODO" uncomment the next two lines to print data info
    #print(f'data: {raw_data}\ntype of the data: {type(raw_data)}')
    #print(f'using json.dumps: {json.dumps(raw_data, indent=4)}')
    print('raw message received . . .')

    RAW_DATA_TOPIC = 'g1-raw-text-data-topic-dev'
    print(f'publishing raw messages to the {RAW_DATA_TOPIC} topic . . .')
    aws_instance_bootstrap_servers = ['b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092',
                                      'b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092']

    producer = KafkaProducer(bootstrap_servers=aws_instance_bootstrap_servers)
    # producer = KafkaProducer(
    #    value_serializer=lambda v: json.dumps(v).encode("utf-8"))

    print(f"article: {raw_data['article']}")
    print(f"keys: {type(raw_data['article'].keys())}")
    print(f"values: {type(raw_data['article'].values())}")
    #producer.send(RAW_DATA_TOPIC, {"text": raw_data['data'][0]})
    print('publishing raw messages completed. . .')


produce_the_message()
