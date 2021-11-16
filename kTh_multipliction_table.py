import json
from itertools import islice

# 668. Kth Smallest Number in Multiplication Table - Hard
# Nearly everyone has used the Multiplication Table. The multiplication table of size m x n 
# is an integer matrix mat where mat[i][j] == i * j (1-indexed).
# Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.
#
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

# binary search approach
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # func to found how many values are smaller than X value inside multi-on table
        # count row by row, using ( i*count <= x )
        def isEnough(x):
            count = 0
            for i in range(1, m+1):
                count += min(n, x//i)
            return k <= count

        # binary search for correct answer value
        # check if mid value can be the answer, than it is high bound, if not, than next value after it must be lower bound of search
        lo, hi = 1, m*n
        while lo<hi:
            mid = (lo+hi) // 2
            if isEnough(mid):
                hi = mid
            else:
                lo = mid+1
                
        return lo

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 3
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.findKthNumber(int(args_raw[0]), int(args_raw[1]), int(args_raw[2]))    

            f_out.write(json.dumps(res) + '\n')
