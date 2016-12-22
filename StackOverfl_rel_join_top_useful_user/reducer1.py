#!/usr/bin/python

# Find the accepted answer for every question and emit only this

import sys

old_keys = [0, 0, 0]

for line in sys.stdin:
    keys = line.strip().split('@')
    if old_keys[0] == keys[0] and old_keys[1] == keys[1]:
        if len(keys) ==3:
            #this is the answer that we were looking for
            userid = keys[2]
            ansid = keys[1]
        elif len(old_keys)==3:
            userid = old_keys[2]
            ansid = old_keys[1]
        print(userid +'@1@' + ansid)
    else:
        old_keys = keys
