#!/usr/bin/python

# Group the same word coming from the same file

import sys

old_prim_key = ''
old_filen = ''
files_dict = {}
for line in sys.stdin:
        keys = line.strip().split(':@')
        prim_key = keys[0]
        num_files = int(keys[1])
        filename_times = keys[2].split(':')
        filename = filename_times[0].split('\'')
        filen = filename[1]
        times = filename_times[1].split('}')
        times_f = int(times[0])

        if prim_key==old_prim_key:
                if old_filen==filen:
                        #update the counter in case we find the same prim_key and the same file
                        old_times_f = files_dict.get(old_filen)
                        files_dict[old_filen] = old_times_f+times_f

        else:
                if old_prim_key:
                        #print all the contents of the dictionary for this prim_key
                        print(old_prim_key + ':@' + str(len(files_dict)) + ':@' + str(files_dict))
                old_prim_key, old_filen = prim_key, filen
                files_dict.clear()
                files_dict.update([(filen, times_f)])

if prim_key:
        print(old_prim_key + ':@' + str(len(files_dict)) + ':@' + str(files_dict))
