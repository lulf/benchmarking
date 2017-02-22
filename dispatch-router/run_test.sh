#/bin/bash
COLLECTOR_HOST=$1
rm -f result.dat

for i in `seq 1 10`
do
    ansible-playbook stop-clients.yaml
    head -n $i routerhosts.orig > routerhosts

    sleep 10
    ansible-playbook start-clients.yaml
    chosts=`cat clienthosts | awk '{ print $0":8080" }' | tr '\n' ','`
    clienthosts=${chosts%?}
    ssh $COLLECTOR_HOST "/root/ebench-collector/bin/ebench-collector -i 60 -I 1 -a $clienthosts" > result_$i.json
done
ansible-playbook stop-clients.yaml
