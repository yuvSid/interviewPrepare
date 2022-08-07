import json

#
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Determine the perimeter of the island.
#
# https://leetcode.com/problems/island-perimeter/

def islandPerimeter(grid: list[list[int]]) -> int:
    p = 0

    for i, each_row in enumerate(grid) :
        for k, each_cell in enumerate(each_row) :
            if (not i) and each_cell : #first row     
                p += 1
            if each_cell != ((i < (len(grid)-1)) and grid[i+1][k]) : #last row or water under
                p += 1
            if (not k) and each_cell :
                p += 1
            if each_cell != ((k < (len(each_row)-1)) and each_row[k+1]):
                p += 1

    return p

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out :
        readen_line = f_in.readline().rstrip()
        while readen_line :
            lst = json.loads(readen_line)

            res = islandPerimeter(lst)    

            f_out.write(json.dumps(res) + '\n')
            readen_line = f_in.readline().rstrip()
