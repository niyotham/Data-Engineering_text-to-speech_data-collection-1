### Create  a `getting_started.ini` fiile here and have the following code in the file
```bash

[default]
bootstrap.servers=<BOOTSRAP SERVER ADDRES>
security.protocol=SASL_SSL
sasl.mechanisms=PLAIN
sasl.username=<YOUR API KEY>
sasl.password=<YOUR API SECRETE KEY>

[consumer]
group.id=python_example_group_1

# 'auto.offset.reset=earliest' to start reading from the beginning of
# the topic if no committed offsets exist.
auto.offset.reset=earliest
```