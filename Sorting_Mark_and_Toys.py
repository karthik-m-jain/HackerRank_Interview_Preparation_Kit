# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:37:18 2020

@author: Karthik Jain
"""

#!/bin/python3

import math
import os
import random
import re
import sys
     
# Complete the maximumToys function below.
def maximumToys(a, k):
    n=len(a)    

    list.sort(a)
    count=0
    for i in range(n):
        if(a[i]<=k):
            count+=1
            k-=a[i]

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()


