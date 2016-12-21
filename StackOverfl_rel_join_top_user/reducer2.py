#!/usr/bin/python

# Pick the user with the max number of answers from all the reducers using the
# sorting of MapReduce. However it consumes all the input as it has to do.

import sys

count = 0
for line in sys.stdin:
        if count == 0:
                #take only the first line
                keys = line.strip().split('@')
                max_q_ids = keys[2]
                if max_q_ids[-1] == '/':
                        max_q_ids = max_q_ids[:-2]
                print(keys[1] + ' -> ' + max_q_ids.replace('//', ', '))
                count += 1
