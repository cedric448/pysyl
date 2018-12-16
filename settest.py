#!/usr/bin/env python3

import sys
inpt = sys.argv[1:]
s = set()

for a in inpt:
    if a not in s:
        s.add(a)

print(s)

