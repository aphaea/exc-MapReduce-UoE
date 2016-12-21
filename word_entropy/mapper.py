#!/usr/bin/python

# Count all the times the 2 word sequence appeared into 3 word sequences
# and emit it

import sys

prev_double_key = ''
prev_double_val = 0
for line in sys.stdin:
        keys = line.strip().split()
        val = int(keys[3])
        double_key = keys[0] + '.' + keys[1]
        if prev_double_key == double_key:
                prev_double_val += val
                print(double_key + '.' + str(val))
        else:
                if prev_double_key:
                        print(prev_double_key + '.' + '0' + str(prev_double_val)+ '/')
                prev_double_key, prev_double_val = double_key, val
                print(double_key + '.' + str(val))

if prev_double_key == double_key:
        print(prev_double_key + '.' + '0' + str(prev_double_val)+ '/')
