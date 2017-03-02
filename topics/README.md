To benchmark topics, the benchmarking agent can be instantiated using the templates for
the [producer](https://github.com/EnMasseProject/openshift-configuration/blob/master/include/topic-producer-template.json) and [consumer](https://github.com/EnMasseProject/openshift-configuration/blob/master/include/topic-consumer-template.json)

Once you have configured a topic, you can instantiate the consumer:

```
oc process -f topic-consumer-template.json ADDRESS=mytopic MESSAGE_SIZE=256 DURATION=3600 REPORT_INTERVAL=30
```

This will create

   * A deployment for the benchmarking agent setting up a consumer of the topic. This can be scaled to test multiple consumers
   * A job for collecting metrics accross all consumers and listening to port 8080
   * A service for connecting to the metrics collector

The metric collector will output a json snapshot of the latest collected metrics (the interval specified by REPORT_INTERVAL). You can also monitor the metrics by looking at the job log

The producer is instantiated in the same way, but with an extra argument controlling the SEND_RATE (0 means max):

```
oc process -f topic-producer-template.json ADDRESS=mytopic MESSAGE_SIZE=256 DURATION=3600 REPORT_INTERVAL=30 SEND_RATE=3000
```

This will create

   * A deployment for the benchmarking agent setting up a producer to the topic. This can be scaled to test multiple producers
   * A job for collecting metrics accross all producers and listening to port 8080
   * A service for connecting to the metrics collector

To access the collector services externally, you can create a route.

This folder also contains a two scripts for testing two use cases:

    1. Single producer at fixed rate, N shards of the broker, then increasing the number of consumers
    2. Single consumer, N shards of the broker, then increasing the number of low-rate producers
