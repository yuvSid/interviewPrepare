# include <vector>
# include <array>
# include <tuple>

// 417. Pacific Atlantic Water Flow - # Medium
// There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
// The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
// The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
// Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

// https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution {
public:
    std::array<std::pair<int, int>, 4> directions = { { {0, -1}, {-1, 0}, {0, 1}, {1, 0} } };
    size_t height = 0;
    size_t width = 0;

    typedef std::vector<std::vector<bool>> visited_vec;

    void exploreElementDFS(int j, int i, Solution::visited_vec& visited, std::vector<std::vector<int>>& heights)
    {
        visited[j][i] = true;

        for (auto& el : directions) {
            int to_j = j+el.first;
            int to_i = i+el.second;

            if (to_j<0 || to_j>=height || to_i<0 || to_i>=width 
            || visited[to_j][to_i] || heights[to_j][to_i] < heights[j][i])
                continue;

            exploreElementDFS(to_j, to_i, visited, heights);
        }
    }

    std::vector<std::vector<int>> pacificAtlantic(std::vector<std::vector<int>>& heights) 
    {
        std::vector<std::vector<int>> result;
        height = heights.size();
        width = heights[0].size();
        // store if element is visited_vec while checking connection to pacific and atlantic separatly
        Solution::visited_vec p_visited(height, std::vector<bool>(width, false));
        Solution::visited_vec a_visited(height, std::vector<bool>(width, false));

        // go through cells connected to oceans using dfs in oriented tree
        for (int j=0; j<height; j++) {
            exploreElementDFS(j, 0, p_visited, heights);
            exploreElementDFS(j, width-1, a_visited, heights);
        }
        for (int i=0; i<width; i++) {
            exploreElementDFS(0, i, p_visited, heights);
            exploreElementDFS(height-1, i, a_visited, heights);
        }

        // Go through all cells to check connection to both oceans
        for (int j=0; j<height; j++)
            for (int i=0; i<width; i++)
                if (p_visited[j][i] && a_visited[j][i])
                    result.push_back(std::vector {j, i});

        return result;        
    }


};