#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_number: int = 999999999999
    max_number: int = 0

    for i in arr:
        if i < min_number:
            min_number = i

    for j in arr:
        if j > max_number:
            max_number = j

    arr_min = arr.copy()
    arr_max = arr.copy()

    arr_min.remove(max_number)
    arr_max.remove(min_number)

    min_sum = sum(arr_min)
    max_sum = sum(arr_max)

    print(min_sum, max_sum)


if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))
    arr = [256741038, 623958417, 467905213, 714532089, 938071625]
    miniMaxSum(arr)
