#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = list(s[:-2].rsplit(':'))
    militar_time = ""

    if "PM" in s:
        hour = int(time[0])
        if 12 + hour == 24:
            time[0] = "12"
        else:
            time[0] = str(12 + hour)
        militar_time = ":".join(time)
    elif "AM" in s:
        if time[0] == "12":
            time[0] = "00"
        militar_time = ":".join(time)

    return militar_time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
