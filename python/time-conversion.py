#!/bin/python3

import math
import os
import random
import re
import sys

from sympy import horner, per

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    [hour, minute, seconds] = re.split(":", s)
    period = re.search("PM",s)
    minus = re.search("-",s)
    if(period and minus):
        hour = "12"
    elif(not period and (minus or int(hour)==12)):
        hour = "00"
    elif(period and int(hour)!=12):
        hour = int(hour)+12

    return(f"{hour}:{minute}:{seconds[0:2]}")

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)
