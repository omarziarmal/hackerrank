#!/bin/python3

import sys

n = int(input().strip())

# if n % 2 == 1    is the same as below
if n % 2 == 1:
    print('Weird')
elif n < 5:
    print('Not Weird')
elif n <= 20:
    print('Weird')
else:
    print('Not Weird')

