from kafka import KafkaProducer
import wavio as ww

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# return tuple containing(data, rate, sampwidth)
x = wav2bytes("bush_read")

# here I 'm sending 3 messages
# data - > nparray
producer.send("TestTopic", key=b'data', value=b'%s' % (x[0]))
# rate - > int
producer.send("TestTopic", key=b'rate', value=b'%d' % (x[1]))
# sampwidth - > int
producer.send("TestTopic", key=b'sampwidth', value=b'%d' % (x[2]))
send("TestTopic", "bush_read")
