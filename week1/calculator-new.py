#!/usr/bin/env python3

import sys

def cal_tax(income):
    tax = 0
    earn = 0
    insurance = income * 16.5 / 100
    b = income - insurance -3500
    if b <= 0:
        tax = 0
    elif b <= 1500:
        tax = b * 0.03
    elif b > 1500 and b <= 4500:
        tax = b * 0.10 - 105
    elif b > 4500 and b <= 9000:
        tax = b * 0.2 - 555
    elif b > 9000 and b <=35000:
        tax = b * 0.25 - 1005
    elif b > 35000 and b <= 55000:
        tax = b * 0.3 - 2755
    elif b > 55000 and b <= 80000:
        tax = b * 0.35 - 5505
    else:
        tax = b * 0.45 - 13505
    earn = income - tax - insurance
    return earn


def print_tax(dict):
    for k, v in dict.items():
        print(k, ':{:.2f}'.format(v))

if __name__ == '__main__':

    try:
        c = {}

        for arg in sys.argv[1:]:
            b = arg.split(':')
            c[int(b[0])] = int(b[1])


        d = {}
        tax = []
        earn = []
        k = list(c.keys())
        v = list(c.values())

        #print(k)
        #print(v)
        for income in v:
            earn.append(cal_tax(income))

        #print(earn)

        len = len(k)

        out = {}

        for index in range(len):
            if index < len:
                out[k[index]] = earn[index]
        #print(out)

        print_tax(out)

    except:
        print('Parameter Error')

