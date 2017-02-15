#!/bin/sh
NUM=`hostname | awk -F "[^0-9]*" '{print $2}'`
ID=$((10#$NUM))
OUT="/etc/sysconfig/network-scripts/ifcfg-p5p1"

ifdown p5p1
cat >$OUT <<EOL
TYPE=Ethernet
BOOTPROTO=static
DEFROUTE=yes
PEERDNS=yes
PEERROUTES=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=no
IPV6_AUTOCONF=no
IPV6_DEFROUTE=no
IPV6_PEERDNS=no
IPV6_PEERROUTES=no
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=p5p1
UUID=2cf9e005-9596-406a-ba68-4828fde3b572
DEVICE=p5p1
ONBOOT=yes
IPADDR=172.16.1.$ID
NETMASK=255.255.128.0
EOL

ifup p5p1
