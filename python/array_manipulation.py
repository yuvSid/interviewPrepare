import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
# https://www.hackerrank.com/challenges/crush/problem
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    
    arr = [0] * n
    for q in queries :
        arr[q[0]-1] += q[2]
        if (q[1] < n) :
            arr[q[1]] -= q[2]

    max_val = arr[0]
    counter_val = 0
    for val in arr :
        counter_val += val
        if max_val < counter_val :
            max_val = counter_val
    return max_val

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    frptr = open('./OUTPUT/IN', 'r')
    fptr = open('./OUTPUT/OUT', 'w')

    first_multiple_input = frptr.readline().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, frptr.readline().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
