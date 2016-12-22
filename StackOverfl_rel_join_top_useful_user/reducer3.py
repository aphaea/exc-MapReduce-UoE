#!/usr/bin/python

# Pick the user with the max number of accepted answers from all the reducers 
# using the sorting of MapReduce. However it consumes all the input as it has to do.

import sys

count = 0
for line in sys.stdin:
        if count == 0:
                #take only the first line
                keys = line.strip().split('@')
                counter = keys[0]
                user = keys[1]
                answer = keys[2]
                print(user + ' -> ' + counter + ', ' + answer)
                count += 1
