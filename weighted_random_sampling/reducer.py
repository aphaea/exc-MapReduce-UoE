#!/usr/bin/python

# Reducer penalizes the lines that came from small files and give advantage
# to those came from large files

import sys
import random
import math
maxnum = -1

for line in sys.stdin:
        keys = line.strip().split('@')
        filesize = int(keys[0])
        fileline = keys[1]
        randnum = random.uniform(0, 1) #[1]
        key_num = math.pow(randnum, 1/filesize) #[1]
        if key_num > maxnum:
                reservoir = fileline.strip()
                maxnum = key_num

print(reservoir)

#[1] Weighted Random Sampling, 2005, Efraimidis, Spirakis, 
# http://utopia.duth.gr/~pefraimi/research/data/2007EncOfAlg.pdf
