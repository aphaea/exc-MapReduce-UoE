#!/usr/bin/python

# Use the automatic sorting of MapReduce

import sys

prev_line=''
curr_line=''
next_line=''
for line in sys.stdin:
        line = line.strip()
        next_line = line
        if curr_line!= next_line and curr_line!= prev_line:
                print(curr_line)
        prev_line = curr_line
        curr_line = next_line

if curr_line!= prev_line:
        print(line)
