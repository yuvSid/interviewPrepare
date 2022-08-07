import json
from typing import Optional
from collections import deque

# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
#  This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
#
# https://leetcode.com/problems/diameter-of-binary-tree/
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.__max_val = 0
    
    def __maximum(self, node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            max_left = self.__maximum(node.left)
            max_right = self.__maximum(node.right)
            self.__max_val = max(self.__max_val, max_left + max_right)
            return 1 + max(max_left, max_right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_root = self.__maximum(root)
        return max(max_root-1, self.__max_val)
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            readen_line = f_in.readline().rstrip()
            if not readen_line:
                break
            tree_raw = json.loads(readen_line)
            
            tree = TreeNode(tree_raw[0])
            next_to_write = deque([tree, tree])
            for node in tree_raw[1:]:
                place = next_to_write.popleft()   
                if node:
                    new_node = TreeNode(node)
                    if place == next_to_write[0]:
                        place.left = new_node
                    else:
                        place.right = new_node
                    next_to_write.extend([new_node, new_node])

            res = Solution.diameterOfBinaryTree(Solution(), tree) # TODO change on real file name    

            f_out.write(json.dumps(res) + '\n')
