#!/usr/bin/env python
#coding=utf-8

import sys

age = sys.argv[1]
a = int(age)
if((a >= 0) and (a < 10)):
    print('you belong to kids')
elif((a >= 10) and (a < 18)):
    print('you belong to teenager')
elif((a >= 18) and (a < 30)):
    print('you belong to adult')
elif((a >= 30) and (a < 60)):
    print('you belong to older')
elif((a >= 60) and (a < 120)):
    print('you belong to oldest')
else:
    pass
