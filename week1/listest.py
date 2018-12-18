#!/usr/bin/env python3

import sys

inpt = sys.argv[1:]
l3 = []
g3 = []

for a in inpt:
    if len(a) <= 3:
        l3.append(a)
    else:
        g3.append(a)

print(l3)
print(g3)

