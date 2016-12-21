#!/usr/bin/python

# Reducer does the join and prints in the same line during different iterations
# it works for Python 2.7

# Output format: George --> (ADBS, 80) (EXC, 70) (TTS, 80)
#                Anna --> (EXC, 65)

import sys

student_n = ''
prev_student_n = ''
sub_tuple = ''

for line in sys.stdin:
        #print (line.strip())
        keys = line.strip().split('.')
        if "0@" in keys[1]:
                prev_student_n = student_n
                name = keys[1].split('0@')
                student_n = name[1]
                if prev_student_n:
                        print('')
                print student_n + ' --> ',
        else:
                val = keys[1].split()
                sub_tuple = '('+ val[0] + ',' + val[1] + ')  '
                print sub_tuple,
