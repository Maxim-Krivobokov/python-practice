# Pull and push data ingestion methods

Instead of making requests, sometimes data can be just pushed towards us.
For examples, Queries (RabbitMQ, Kafka, etc.)

# We must use docker to deploy nats server locally
(nats is open-source cloud-native messaging system)

```docker run --rm -d --publish=4222:4222 nats```
or podman:
```podman run --rm -d --publish=4222:4222 nats```

## Note:
lib pynats is used and NATSClient

# Spammer.py
sends messages to the nats server.
It reads "taxi" database and send to the nats server

# event_client
reads messages from nats server and print to stdout
