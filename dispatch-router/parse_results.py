#!/usr/bin/env python

import sys
import json

result_files = sys.argv[1:]

for f in result_files:
    fh = open(f, 'r')
    raw = fh.read()
    content = json.loads(raw)
    print(content["throughput"])
