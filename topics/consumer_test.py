#!/usr/bin/env python3
import time
import benchmark

MAX_SHARDS=4
MAX_CONSUMERS=16
ADDRESS="a"
INTERVAL=96
PRODUCER_URL="http://metrics.10.12.56.17.nip.io/metrics/producer"
CONSUMER_URL="http://metrics.10.12.56.17.nip.io/metrics/consumer"
OUTPUT_FILE="consumer_test_result.dat"

f = open(OUTPUT_FILE, "w")

f.write("#shards consumers consumer_throughput producer_throughput producer_response_max producer_response_99p\n")
for shards in range(1, MAX_SHARDS + 1):
    benchmark.reset(ADDRESS)
    num_pods = benchmark.scale_and_wait(ADDRESS, shards)
    time.sleep(60)
    for consumers in range(1, MAX_CONSUMERS + 1):
        benchmark.scale_and_wait("benchmark-consumer", consumers, num_pods)
        benchmark.scale_and_wait("benchmark-producer", 1, num_pods + consumers)

        time.sleep(INTERVAL)

        consumer_metrics = benchmark.fetch_metrics(CONSUMER_URL)
        producer_metrics = benchmark.fetch_metrics(PRODUCER_URL)
        c_throughput = consumer_metrics["throughput"]
        p_throughput = producer_metrics["throughput"]
        p_maxresponse = producer_metrics["latencies"]["max"]
        p_99presponse = producer_metrics["latencies"]["99p"]

        f.write("%d %d %.2f %.2f %.2f %.2f\n" % (shards, consumers, float(c_throughput), float(p_throughput), float(p_maxresponse), float(p_99presponse)))
        f.flush()

        benchmark.scale_and_wait("benchmark-producer", 0, num_pods + consumers)
        benchmark.scale_and_wait("benchmark-consumer", 0, num_pods)

benchmark.reset(ADDRESS)
f.close()
