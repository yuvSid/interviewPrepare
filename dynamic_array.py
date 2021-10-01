import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
# https://www.hackerrank.com/challenges/dynamic-array/problem
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries) -> list[int]:
    lastAnswer = 0
    result = []
    arr = [[] for _ in range(n)]
    
    for querie in queries :
        idx = (querie[1] ^ lastAnswer) % n            
        
        if querie[0] == 1 :
            arr[idx].append(querie[2])
        elif querie[0] == 2 :
            lastAnswer = arr[idx][querie[2] % len(arr[idx])]
            result.append(lastAnswer)
        else :
            print('Wrong command in querie')    
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
