#!/usr/bin/python

# Find all the answers, the user that answered and the corresponding question
# and emit it per user

import sys
import re


for line in sys.stdin:
    line = line.strip()
    m = re.search('PostTypeId=\"([0-9])?\"', line)
    if int(m.group(1))==2:
        m = re.search(' ParentId=\"([0-9]*)\"(.*)OwnerUserId=\"([0-9]*)\"', line)
        questionid = m.group(1)
        user = m.group(3)
        print(user + '@1@' + questionid)
