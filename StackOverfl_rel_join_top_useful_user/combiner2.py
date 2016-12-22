#!/usr/bin/python

# Group the accepted answers by user

import sys

old_user = ''
user_counter = 0
a_ids = ''

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
            a_ids = a_ids[:-2]
            print(old_user + '@' + str(user_counter) + '@' + a_ids)
        old_user, user_counter = user, counter
        a_ids = ''
        a_ids += answer + '//'

if user:
    a_ids = a_ids[:-2]
    print(old_user + '@' + str(user_counter) + '@' + a_ids)
