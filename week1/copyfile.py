#!/usr/bin/env python3

import sys

def copy_file(src, dst):
    with open(src, 'r') as src_file:
        with open(dst, 'w') as dst_file:
            #linelist = []
            #linelist.append(src_file.readlines())
            for i,x in enumerate(src_file.readlines()):
                #if (i == 0):
                    #continue
                #else:
                linelist = str(i + 1) + ' ' + x
                dst_file.write(linelist)

if __name__ == '__main__':
    copy_file('shiyanlou.txt', 'shiyanlou_copy.txt')

