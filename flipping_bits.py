#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    binary = bin(n)[2:].zfill(32)
    new_binary = ''
    for bit in binary:
        if bit == '1':
            new_binary += '0'
        elif bit == '0':
            new_binary += '1'
    decimal = int(new_binary, 2)
    return decimal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
