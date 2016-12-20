#!/usr/bin/python

# Use the sorting of MapReduce and take the top 20 of all the mappers

import sys

count_list = 0
for line in sys.stdin:
        if count_list < 20:
                tok = line.strip().split('\t')
                print(tok[0] + ' ' + tok[1])
                count_list += 1
        else:
                continue
