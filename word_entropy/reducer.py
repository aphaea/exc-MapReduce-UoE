#!/usr/bin/python

# Sorting with ASCII, distinguish the counter of 2 word sequence and find the
# probability of the 3rd word and finally calculate the entropy of the 2-word-seq

import sys
import math


prev_double_key = ''
sum_k=0
entropy_k = 0
for line in sys.stdin:
        keys = line.strip().split('.')
        double_key = keys[0] + ' ' + keys[1]
        if prev_double_key == double_key:
                if "/" not in keys[2]:
                        freq_k = int(keys[2])
                        pos_k = float(freq_k)/sum_k
                        entropy_k = entropy_k - (pos_k * math.log(pos_k, 2))
                else:
                        num = keys[2].split('/')
                        sum_k = sum_k + int(num[0])

        else:
                if prev_double_key:
                        print(prev_double_key + '\t' + str(entropy_k))
                prev_double_key = double_key


                entropy_k = 0
                num = keys[2].split('/')
                sum_k = int(num[0])

if prev_double_key == double_key:
        print(prev_double_key + '\t' + str(entropy_k))
