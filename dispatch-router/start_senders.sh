#!/bin/sh
set -x
HOSTS=`cat /root/routerhosts | shuf | tr '\n' ','`

/root/start_sender.sh 8 256 3000 "$HOSTS"

