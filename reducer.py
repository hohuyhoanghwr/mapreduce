#!/usr/bin/env python

import sys

previous_key = None
count = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    key, value = data

    if previous_key is not None and previous_key != key:
        if count > 114:
            sys.stdout.write("{0}\t{1}\n".format(previous_key, count))
        count = 0

    count += 1
    previous_key = key

# Handle the last key
if previous_key is not None and count > 114:
    sys.stdout.write("{0}\t{1}\n".format(previous_key, count))

