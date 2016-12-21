#!/usr/bin/python

''' 
File format:

student 1 George
mark 1 EXC 70
student 2 Anna
mark 1 ADBS 80
mark 2 EXC 65
mark 1 TTS 80

Distinguish the students and the marks and emit them
'''


import sys

for line in sys.stdin:
        keys = line.strip().split()
        if keys[0] == 'student':
                print(keys[1] + '.' + '0@' + keys[2])
        else:
                if keys[0] == 'mark':
                        print(keys[1] + '.' + keys[2] + '.' +keys[3])
