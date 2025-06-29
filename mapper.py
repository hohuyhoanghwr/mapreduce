#!/usr/bin/env python

import sys

# Process each line from standard input
for line in sys.stdin:
    data = line.strip().split("\t")

    # Skip lines that do not have exactly 6 columns
    if len(data) != 6:
        raise ValueError(f"Invalid input line (expected 6 columns): {line}")

    date, time, item, category, sales, payment = data

    try:
        sales_value = float(sales)
        # Emit category as key and sales as value
        sys.stdout.write("{0}\t{1}\n".format(category, sales_value))
    except ValueError:
        continue

