#!/usr/bin/python

# Use the sorting given by MapReduce, count all the three word sequences

import fileinput

prev_word = ''
prev_counter = 0
for line in fileinput.input():
        word, countw = line.strip().split('\t')
        countw = int(countw)
        if prev_word == word:
                prev_counter += countw
        else:
                if prev_word:
                        print(prev_word + '\t' + str(prev_counter))
                prev_word, prev_counter = word, countw

if prev_word == word:
        print(prev_word + '\t' +str(prev_counter))