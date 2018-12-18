#!/usr/bin/env python3

import sys

try:
    Tax = 0
    Income = int(sys.argv[1])
    b = Income - 3500
    if b <= 1500:
        Tax = b*0.03
    elif b > 1500 and b <= 4500:
        Tax = b*0.1 - 105
    elif b > 4500 and b <= 9000:
        Tax = b*0.2 - 555
    elif b > 9000 and b <= 35000:
        Tax = b*0.25 - 1005
    elif b > 35000 and b <= 55000:
        Tax = b*0.3 - 2755
    elif b > 55000 and b <= 80000:
        Tax = b*0.35 - 5505
    else:
        Tax = b*0.45 - 13505
    print(format(Tax, '.2f'))
except:
    print('Parameter Error')
