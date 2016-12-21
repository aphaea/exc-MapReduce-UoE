#!/usr/bin/python

# Group all the unique answers by user and count them, keep the user with the
# maximum number of answers and emit him/her at the end

import sys

old_user = ''
user_counter = 0
max_counter = -1
max_q_ids = ''
max_user = ''
qset = set()

for line in sys.stdin:
    keys = line.strip().split('@')
    user = keys[0]
    counter = int(keys[1])
    question = keys[2]

    if user==old_user:
        qset.update(question.split('//'))
        user_counter = len(qset)
    else:
        if old_user:
            if user_counter > max_counter:
                max_user = old_user
                max_counter = user_counter
                max_q_ids = sorted(qset)
        old_user= user
        qset.clear()
        qset.update(question.split('//'))
        user_counter = len(qset)

if user:
    if user_counter > max_counter:
        max_user = old_user
        max_counter = user_counter
        max_q_ids = sorted(qset)

str_to_prnt = str(max_counter) + '@' + max_user + '@'
for i in range(0, len(max_q_ids)):
        str_to_prnt += max_q_ids[i] + '//'
if str_to_prnt[-1] == '/':
        str_to_prnt = str_to_prnt[:-2]
print(str_to_prnt)
