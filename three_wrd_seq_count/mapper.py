#!/usr/bin/python

# Find all the three word sequences

import sys

for line in sys.stdin:
        tok = line.strip().split()
        if len(tok)>2:
                for i in range(1, len(tok)-1):
                        word1, word2, word3 = tok[i-1], tok[i], tok[i+1]
                        word_str = word1 + " " + word2 + " " + word3
                        print(word_str + "\t1")
                else:
                        continue
