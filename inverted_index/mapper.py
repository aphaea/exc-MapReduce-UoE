#!/usr/bin/python

# Identifies all the words that a file contains

import sys
import re
import os

for line in sys.stdin:
        keys = line.strip().split()
        for i in range(0, len(keys)):
                if keys[i]:
                        path_to_file = str(os.environ["mapreduce_map_input_file"])
                        m = re.search('//(.*)/(.*)', path_to_file)
                        print(keys[i] + ' :@1:@'+ '{\'' + m.group(2) + '\': 1}')
