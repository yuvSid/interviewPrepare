import json
from itertools import islice

# 417. Pacific Atlantic Water Flow - # Medium
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.height, self.width = len(heights), len(heights[0])
        # data for element is (visited, connected to pacific, connected to atlantic)
        p_visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        a_visited = [[False for _ in range(self.width)] for _ in range(self.height)]

        for i in range(self.width):
            #explore horizontal ocean connections
            self.exploreElementDFS(0, i, p_visited, heights)
            self.exploreElementDFS(self.height-1, i, a_visited, heights)

        for j in range(self.height):
            #explore vertical ocean connections
            self.exploreElementDFS(j, 0, p_visited, heights)
            self.exploreElementDFS(j, self.width-1, a_visited, heights)

        # go through matrix to check connections
        res = []
        for j in range(self.height):
            for i in range(self.width):
                if p_visited[j][i] and a_visited[j][i]:
                    res.append([j, i])

        return res

    def exploreElementDFS(self, j, i, visited, data):
        visited[j][i] = True

        for el in self.directions:
            to_j, to_i = j+el[0], i+el[1]
            
            if (to_j < 0 or to_j >= self.height or to_i < 0 or to_i >= self.width 
            or visited[to_j][to_i] or data[to_j][to_i] < data[j][i]):
                continue
        
            self.exploreElementDFS(to_j, to_i, visited, data)
            

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.pacificAtlantic(json.loads(args_raw[0]))    

            f_out.write(json.dumps(res) + '\n')
