import json
from itertools import islice
# 994. Rotting Oranges - # Medium
# You are given an m x n grid where each cell can have one of three values:
#     0 representing an empty cell,
#     1 representing a fresh orange, or
#     2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        next_min = []
        width, height = len(grid[0]), len(grid)
        
        for line in range(height):
            for cell in range(width):
                 if grid[line][cell] == 2:
                    next_min.append((line, cell))
        
        mins = 0
        while next_min:
            cur_min = next_min
            next_min = []

            for (l, c) in cur_min:
                check = [(l-1, c), (l+1, c), (l, c+1), (l, c-1)]
                for (i, j) in check:
                    if ( i>=0 and i<height and j>=0 and j<width) and grid[i][j] == 1:
                        grid[i][j] = 2
                        next_min.append((i, j))

            if next_min:
                mins += 1

        for line in grid:
            for cell in line:
                if cell == 1:
                    return -1
        return mins    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.orangesRotting(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
