import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
# https://www.hackerrank.com/challenges/2d-array/problem
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr : list[list[int]]) -> int:
    sumList = []
    for i in range(2, len(arr)) :
        for k in range(2, len(arr[i])) :
            summ = sum(arr[i-2][k-2: k+1])
            summ += arr[i-1][k-1]
            summ += sum(arr[i][k-2 : k+1])
            sumList.append(summ)
    return max(sumList)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()