# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 22:24:10 2020

@author: Karthik Jain
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    #since range is from -9 to 9
    result=-63
    # till 4 because the pattern gonna go till there only
    for i in range(4):
        for j in range(4):
            add=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            result = max(result,add)

    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
