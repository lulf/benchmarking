#!/bin/sh
rm -f result.dat
for i in `seq 1 10`
do
    throughput=`python parse_results.py result_$i.json`
    echo "$throughput" >> result.dat
done
