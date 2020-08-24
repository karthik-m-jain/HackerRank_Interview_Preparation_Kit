# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:10:54 2020

@author: Karthik Jain
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    """
    Alternate solution
    n=len(a)
    for i in range(d):
        temp1=a[0]
        for j in range(1,n):
            a[j-1]=a[j]
        a[n-1]=temp1
    return a"""
    
    b=a[d:]+a[:d]
    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

