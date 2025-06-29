#!/usr/bin/env python

import sys

previous_key = None
sum_sales = 0.0
count = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    key, value = data

    try:
	sale = float(value)
    except ValueError:
	continue

    if previous_key is not None and previous_key != key:
	average = sum_sales / count if count != 0 else 0
        sys.stdout.write("{0}\t{1:.2f}\n".format(previous_key, average))
        sum_sales = 0.0
        count = 0

    sum_sales += sale
    count += 1
    previous_key = key

# Final category
if previous_key is not None and count != 0:
    average = sum_sales / count
    sys.stdout.write("{0}\t{1:.2f}\n".format(previous_key, average))
