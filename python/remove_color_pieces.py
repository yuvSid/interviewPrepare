import json

# 2038. Remove Colored Pieces if Both Neighbors are the Same Color - # Medium
# There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. 
# You are given a string colors of length n where colors[i] is the color of the ith piece.
# Alice and Bob are playing a game where they take alternating turns removing pieces from the line.
# In this game, Alice moves first.
#     Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
#     Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
#     Alice and Bob cannot remove pieces from the edge of the line.
#     If a player cannot make a move on their turn, that player loses and the other player wins.
# Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.
#
# https://leetcode.com/contest/biweekly-contest-63/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        prev_color, color_count = colors[0], 1
        a_moves = b_moves = 0
        for color in colors[1:]:
            if color == prev_color:
                color_count += 1
                if color_count >= 3:
                    if color == 'A':
                        a_moves += 1
                    else:
                        b_moves += 1
            else:
                prev_color = color
                color_count = 1
        
        return a_moves > b_moves
    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            readen_line = f_in.readline().rstrip()
            if not (readen_line):
                break
            readen = json.loads(readen_line)

            exec = Solution()
            res = exec.winnerOfGame(readen)    

            f_out.write(json.dumps(res) + '\n')
