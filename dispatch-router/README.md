# benchmarking
Various scripts used for benchmarking

## To benchmark router

Run the following playbooks to install router and clients:

    ansible-playbook install-router.yaml
    ansible-playbook install-client.yaml

Then you must generate the router config that is to be installed. The `full-network` folder contains
a script for generating a mesh router config based on a list of hosts.

    ./full-network/generate_mesh.sh host1:ip1 host2:ip2 host3:ip3

This will create a folder 'generated' containing the router configs for each host. To copy the
configs:

    ansible-playbook copy-config.yaml

This will ensure that the appropriate host configuration is made ready on each router node. You can
now start the routers

    ansible-playbook start-router.yaml

Once this is done, you can run your test. The `run_test.sh` script runs a benchmark against 1 to 10
routers (assuming you have that many) by picking a set of hosts from the file `routerhosts.orig`,
which contains a list of router hostnames, and lauching the clients against those hosts. The script
will stop and start clients between each configuration of router hosts. The results will be stored
in `result_*.json`.

It also takes as argument one of the client hosts to collect the benchmark results.

    ./run_test.sh my.client.host.com
