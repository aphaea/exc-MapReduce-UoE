#!/usr/bin/python

# Samples a random line from the different files and passes it to the 
# reducer phase

import sys
import random

line_number = 0
line_count = 0

for line in sys.stdin:
        line_count += 1
        if random.randint(0, line_number) == 0:
                resevoir = line.strip()
                line_number += 1

print(str(line_count) + '@' + resevoir)
