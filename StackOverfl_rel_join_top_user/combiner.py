#!/usr/bin/python

# Group the answers by the user that answered using the sorting after the Map
# phase of MapReduce

import sys

old_user = ''
old_question = ''
user_counter = 0
max_counter = -1
q_ids = ''

for line in sys.stdin:
    keys = line.strip().split('@')
    user = keys[0]
    counter = int(keys[1])
    question = keys[2]

    if user==old_user:
        if question != old_question:
            user_counter += counter
            q_ids += question + '//'
    else:
        if old_user:
            if q_ids[-1] == '/':
                q_ids = q_ids[:-2]
            print(old_user + '@' + str(user_counter) + '@' + q_ids)
        old_user, user_counter, old_question = user, counter, question
        q_ids = ''
        q_ids += question + '//'
    old_question = question

if user:
    if q_ids[-1] == '/':
        q_ids = q_ids[:-2]
    print(old_user + '@' + str(user_counter) + '@' + q_ids)
