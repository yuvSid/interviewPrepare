from __future__ import annotations

import json
from typing import Optional

# 993. Cousins in Binary Tree - # Easy
# Given the root of a binary tree with unique values and the values of two different nodes
# of the tree x and y, return true if the nodes corresponding to the values x and y 
# in the tree are cousins, or false otherwise. Two nodes of a binary tree are cousins 
# if they have the same depth with different parents. Note that in a binary tree, 
# the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
#
# https://leetcode.com/problems/cousins-in-binary-tree/

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def buildFromList(self, raw: list) -> TreeNode:
        self.val = raw[0]
        next_to_write = deque([self, self])
        for node in raw[1:]:
            place = next_to_write.popleft()   
            if node:
                new_node = TreeNode(node)
                if place == next_to_write[0]:
                    place.left = new_node
                else:
                    place.right = new_node
                next_to_write.extend([new_node, new_node])

        return self

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        cur_line = deque([(root, root),])
        next_line = deque()
        depth = 0
        x_found = y_found = None
        while cur_line or next_line:
            if not cur_line:
                if x_found or y_found:
                    break
                cur_line, next_line = next_line, cur_line
                depth += 1  
            
            tuple_node = cur_line.popleft()
            if not tuple_node[0]:
                continue

            if tuple_node[0].val == x:
                x_found = tuple_node
            elif tuple_node[0].val == y:
                y_found = tuple_node
            
            if x_found and y_found:
                break

            next_line.extend([(tuple_node[0].left, tuple_node[0]), (tuple_node[0].right, tuple_node[0])])


        return True if (x_found and y_found and x_found[1] != y_found[1]) else False    
    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            tree_line = f_in.readline().rstrip()
            x_line = f_in.readline().rstrip()
            y_line = f_in.readline().rstrip()
            if not (tree_line and x_line and y_line):
                break
            raw_tree = json.loads(tree_line)
            tree = TreeNode.buildFromList(TreeNode(), raw_tree)
        
            exec = Solution()
            res = exec.isCousins(tree, int(x_line), int(y_line))    

            f_out.write(json.dumps(res) + '\n')
