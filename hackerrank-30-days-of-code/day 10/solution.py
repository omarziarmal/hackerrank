#!/bin/python3
import sys

n = int(input().strip())

current_cosecutive_1s = 0
max_cosecutive_1s = 0
while n > 0:
    remainder = n % 2
    if remainder == 1:
        current_cosecutive_1s += 1
        if current_cosecutive_1s > max_cosecutive_1s:
            max_cosecutive_1s = current_cosecutive_1s
    else:
        current_cosecutive_1s = 0

    n = n // 2

print(max_cosecutive_1s)
