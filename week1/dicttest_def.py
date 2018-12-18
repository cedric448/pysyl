#!/usr/bin/env python3

import sys

output_dict = {}

def handle_data(a):
    b = a.split(':')
    output_dict[b[0]] = b[1]
    return output_dict

def print_data(m, n):
    print('ID:', m, 'Name:', n)






if __name__ == '__main__':

    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in output_dict:
        print_data(key, output_dict[key])

