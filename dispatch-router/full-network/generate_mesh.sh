#!/bin/sh
HOSTNAMES=$@

mkdir -p generated
i=0
GENERATED=""
for entry in $HOSTNAMES
do
    echo $i
    name="Router_$i"
    host=`echo $entry | cut -d ':' -f 1`
    ip=`echo $entry | cut -d ':' -f 2`
    cat router_template.conf | ROUTER_ID=$name envsubst > generated/router_$host.conf
    for generated in $GENERATED
    do
        cat connector_template.conf | CONNECTOR_HOST=$generated envsubst >> generated/router_$host.conf
    done
    GENERATED="$GENERATED $ip"
    i=$((i + 1))
done
