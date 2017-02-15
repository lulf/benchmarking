#!/bin/sh
set -x
HOSTS=`cat /root/routerhosts | shuf | tr '\n' ','`

/root/start_receiver.sh 8 1024 3000 "$HOSTS"

