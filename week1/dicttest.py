#!/usr/bin/env python3

import sys

cc = {}
l = list()
inpt = sys.argv[1:]

for a in inpt:
    l.append(a)

for b in l:
    ss = b.split(':')
    cc[ss[0]] = ss[1]

for k,v in cc.items():
    print('ID:',k,'Name:',v)

