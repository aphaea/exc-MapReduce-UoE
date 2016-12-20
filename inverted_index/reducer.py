#!/usr/bin/python

# Group the same words and count their instances in the different files

import sys
import re

old_prim_key = ''
old_filen = ''
files_dict = {}
for line in sys.stdin:
        keys = line.strip().split(':@')
        prim_key = keys[0].strip()
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
                        #else update the dictionary for this prim_key in order to include the new file
                        files_dict.update([(filen, times_f)])
        else:
                if old_prim_key:
                        key_list = list(files_dict.keys())
                        key_list = sorted(key_list)
                        #format of the output
                        str_to_print = old_prim_key + ' : ' + str(len(files_dict)) + ' : {'
                        for i in range(0, len(key_list)):
                            num_ff = files_dict.get(key_list[i])
                            str_to_print += '(' + key_list[i] + ', ' + str(num_ff) + ')//'
                        if str_to_print[-1] == '/':
                                str_to_print = str_to_print[:-2]
                        str_to_print += '}'
                        print(str_to_print.replace('//', ', '))
                old_prim_key, old_filen = prim_key, filen
                files_dict.clear()
                files_dict.update([(filen, times_f)])


if prim_key:
        key_list = list(files_dict.keys())
        key_list = sorted(key_list)
        str_to_print = old_prim_key + ' : ' + str(len(files_dict)) + ' : {'
        for i in range(0, len(key_list)):
                num_ff = files_dict.get(key_list[i])
                str_to_print += '(' + key_list[i] + ', ' + str(num_ff) + ')//'
        if str_to_print[-1] == '/':
                str_to_print = str_to_print[:-2]
        str_to_print += '}'
        print(str_to_print.replace('//', ', '))
