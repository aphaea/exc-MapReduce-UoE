#!/usr/bin/python

# Find the user with the maximum number of accepted answers per reducer

import sys

old_user = ''
old_answer = ''
user_counter = 0
max_counter = -1
a_ids = ''
max_a_ids = ''
max_user = ''

for line in sys.stdin:
    keys = line.strip().split('@')
    user = keys[0]
    counter = int(keys[1])
    answer = keys[2]

    if user==old_user:
        user_counter += counter
        a_ids += answer + '//'
    else:
        if old_user:
            if user_counter > max_counter:
                max_user = old_user
                max_counter = user_counter
                max_a_ids = a_ids
        old_user, user_counter, old_answer = user, counter, answer
        a_ids = ''
        a_ids += answer + '//'
    old_answer = answer

if user:
    if answer != old_answer:
        user_counter += counter
        a_ids += answer + '//'
    if user_counter > max_counter:
        max_user = old_user
        max_counter = user_counter
        max_a_ids = a_ids

if max_a_ids[-1] == '/':
        max_a_ids = max_a_ids[:-2]
print(str(max_counter) + '@' + max_user + '@' + max_a_ids.replace('//', ', '))
