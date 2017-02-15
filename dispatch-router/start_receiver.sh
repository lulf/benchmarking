#!/bin/sh
NUMCLIENTS=$1
MSGSIZE=$2
DURATION=$3
HOSTS=$4

/root/ebench-agent/bin/ebench-agent -a node1 -d $DURATION -h $HOSTS -m $MSGSIZE -s 0 -r $NUMCLIENTS
