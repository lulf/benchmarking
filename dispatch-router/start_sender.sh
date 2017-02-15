#!/bin/sh
NUMCLIENTS=$1
MSGSIZE=$2
DURATION=$3
HOSTS=$4

/root/ebench-agent/bin/ebench-agent -a node1 -d $DURATION -f none -h $HOSTS -m $MSGSIZE -r 0 -s $NUMCLIENTS
