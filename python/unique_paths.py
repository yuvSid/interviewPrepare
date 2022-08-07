import json
from itertools import islice

# 62. Unique Paths - Medium
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
#
# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0]*n for _ in range(m)]
        res[0][0] = 1 #first path
        for j in range(m):
            for i in range(n):
                if (i+1)<n:
                    res[j][i+1] += res[j][i]
                if (j+1) < m:
                    res[j+1][i] += res[j][i]

        return res[m-1][n-1]

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 2
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.uniquePaths(int(args_raw[0]), int(args_raw[1]))    

            f_out.write(json.dumps(res) + '\n')
