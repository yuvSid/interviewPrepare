import json
from itertools import islice

from typing import Optional
from _structs_leetcode import TreeNode

from collections import deque

# 226. Invert Binary Tree - # Easy
# Given the root of a binary tree, invert the tree, and return its root.
#
# https://leetcode.com/problems/invert-binary-tree/

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        invert = deque([root])
        while invert:
            node = invert.popleft()
            if node:
                node.left, node.right = node.right, node.left
                invert.extend([node.left, node.right])
        
        return root

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 1
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.invertTree(TreeNode.buildFromList(TreeNode(), json.loads(args_raw[0])))    

            f_out.write(json.dumps(res.toList() if res else []) + '\n')
