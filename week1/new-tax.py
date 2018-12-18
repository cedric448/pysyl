#!/usr/bin/env python3

import sys

def print_tax(num, income):



def cal_tax(income):
    tax = 0
    insurance = income * 16.5 / 100
    b = income - insurance
    if b <= 1500:
        tax = b*0.03
    elif b > 1500 and b <=4500:
        tax = b*0.1 -105
    elif b > 4500 and b <=9000:
        tax = b*0.2 - 555
    elif b > 9000 and b <=35000:
        tax = b*0.25 - 1005
    elif b > 35000 and b <=55000:
        tax = b *0.3 - 2755
    elif b > 55000 and b <=80000:
        tax = b * 0.35 - 5505
    else:
        tax = b * 0.45 -13505
    return tax



if __name__ == '__main__':
    dict = {sys.argv[1:]}

