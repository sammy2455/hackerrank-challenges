#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    denominator = len(arr)
    positive = 0
    negative = 0
    zeros = 0

    for i in arr:
        if i == 0:
            zeros += 1
        elif i > 0:
            positive += 1
        elif i < 0:
            negative += 1

    print(f'{positive/denominator:.6f}')
    print(f'{negative/denominator:.6f}')
    print(f'{zeros/denominator:.6f}')


if __name__ == '__main__':
    # n = int(input().strip())
    n = 8
    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, -1, -2, -3, 0, 0]
    plusMinus(arr)
