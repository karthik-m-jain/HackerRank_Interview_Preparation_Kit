# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:41:25 2020

@author: Karthik Jain
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count=0
    i=0
    n=len(c)
    while(i<n-1):
        if(i+2<n and c[i+2]==0):
            i+=2
            count+=1
        else:
            i+=1
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
