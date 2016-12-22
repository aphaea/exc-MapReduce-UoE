#!/usr/bin/python

# Find all the questions and the answers and emit them using different format

import sys
import re


for line in sys.stdin:
    line = line.strip()
    m = re.search('PostTypeId=\"([0-9])?\"', line)
    if int(m.group(1))==1:
        if " AcceptedAnswerId=" not in line:
            continue
        else:
            m = re.search(' Id=\"([0-9]*)\"(.*) AcceptedAnswerId=\"([0-9]*)\"', line)
            questid = m.group(1)
            acc_answ = m.group(3)
            print( questid + '@' + acc_answ)
    elif int(m.group(1))==2:
        m = re.search(' Id=\"([0-9]*)\"(.*) ParentId=\"([0-9]*)\"(.*) OwnerUserId=\"([0-9]*)\"', line)
        ansid = m.group(1)
        questid = m.group(3)
        userid = m.group(5)
        print(questid + '@' + ansid + '@' + userid)
