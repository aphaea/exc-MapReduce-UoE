#!/usr/bin/python

# Find the top 20 of each mapper and emit them

import sys

final_list = []
count_list = 0
for line in sys.stdin:
        tok = line.strip().split('\t')
        if count_list != 20:
                final_list.append((tok[1], tok[0]))
                count_list +=1
        else:
                #find the minimum of the list
                min_list = min(final_list, key = lambda t: int(t[0]))
                if int(min_list[0]) < int(tok[1]):
                        final_list[final_list.index(min_list)] = (tok[1], tok[0])

for i in range(0,20):
        print('\t'.join(final_list[i]))