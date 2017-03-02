#!/usr/bin/env python3
# This script assumes that you've logged in to your cluster destination with the oc tool and that
# the current project is the EnMasse project. It also assumes that the producer and consumer
# templates have been set up
import subprocess
import urllib.request
import json

def scale(deployment, replicas):
    subprocess.call(["oc", "scale", "--replicas=" + str(replicas), "deployment", deployment], stdout=subprocess.DEVNULL)

def wait_for_running_pods(num_pods):
    actual_pods = 0
    # print("Waiting for " + str(num_pods) + " pods")
    while actual_pods != num_pods:
        p1 = subprocess.Popen(["oc", "get", "pods"], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "Running"], stdin=p1.stdout, stdout=subprocess.PIPE)
        p3 = subprocess.Popen(["wc", "-l"], stdin=p2.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        output = p3.communicate()[0]
        actual_pods = int(output)
        # print("Output: " + str(output) + " actual_pods= " + str(actual_pods))

def wait_for_pods(num_pods):
    actual_pods = 0
    # print("Waiting for " + str(num_pods) + " pods")
    while actual_pods != num_pods:
        p1 = subprocess.Popen(["oc", "get", "pods"], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["grep", "-v", "STATUS"], stdin=p1.stdout, stdout=subprocess.PIPE)
        p3 = subprocess.Popen(["wc", "-l"], stdin=p2.stdout, stdout=subprocess.PIPE)
        p1.stdout.close()
        output = p3.communicate()[0]
        actual_pods = int(output)
        # print("Output: " + str(output) + " actual_pods= " + str(actual_pods))

def scale_and_wait(deployment, replicas, current_pods=BASE_PODS):
    scale(deployment, replicas)
    expected_pods = current_pods + replicas
    wait_for_running_pods(expected_pods)
    return expected_pods

def reset(address):
    scale(address, 0)
    scale("benchmark-producer", 0)
    scale("benchmark-consumer", 0)
    expected_pods = BASE_PODS
    wait_for_pods(expected_pods)

def fetch_metrics(url):
    return json.loads(urllib.request.urlopen(url).read().decode("utf-8"))
