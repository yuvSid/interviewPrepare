import json
from itertools import islice
from typing import Optional
from _structs_leetcode import TreeNode

# 222. Count Complete Tree Nodes - # Medium
# Given the root of a complete binary tree, return the number of the nodes in the tree.
# According to Wikipedia, every level, except possibly the last, 
# is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. 
# It can have between 1 and 2h nodes inclusive at the last level h.
# Design an algorithm that runs in less than O(n) time complexity.
#
# https://leetcode.com/problems/count-complete-tree-nodes/

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:  
        if not root: # empty tree
            return 0
        if not root.left:
            return 1 # one node case
        
        node, height = root.left, 1
        while node := node.left:
            height += 1
        count = 2**height - 1 # nodes at full levels
        
        node = root
        while height >= 0:
            node_check, height_check = node.right, 0
            while node_check: #find right most node height
                height_check += 1
                node_check = node_check.right
            if height_check == height:
                count += 2**height # low level is full too
                break
            
            node_check, height_check = node.right, 0
            while node_check: # find left most of right half node height
                height_check += 1
                node_check = node_check.left
            if height_check == height: # check right half to found needed val
                node = node.right
                count += 2**(height-1)
            else:
                node = node.left # check left half
            
            height -= 1

        return count
                

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.countNodes(TreeNode.buildFromList(TreeNode(), json.loads(args_raw[0])))    

            f_out.write(json.dumps(res) + '\n')
