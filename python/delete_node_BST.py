import json
from itertools import islice

# 450. Delete Node in a BST - Medium
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
# Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
#     Search for a node to remove.
#     If the node is found, delete the node.

from typing import Optional
from _structs_leetcode import TreeNode

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        del_node = parent = None        
        
        check = root
        while (check):
            if check.val == key:
                del_node = check
                break
            else:                
                parent = check
                if key < check.val:
                    check = check.left
                else:
                    check = check.right

        if (del_node):
            new_child = None
            if (del_node.right): # right child exist, need to find new place for left child of del node
                new_place_for_left = del_node.right
                while (new_place_for_left.left):
                    new_place_for_left = new_place_for_left.left
                new_place_for_left.left = del_node.left
                new_child = del_node.right
            elif (del_node.left): # no right node in del_node
                new_child = del_node.left
            
            if (parent): # found not at top node
                if (key < parent.val):
                    parent.left = new_child
                else:
                    parent.right = new_child
            else:
                root = new_child


        return root  
    

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 2
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.deleteNode(TreeNode.buildFromList(TreeNode(), json.loads(args_raw[0])), int(args_raw[1]))    

            f_out.write(json.dumps(res.toList() if res else []) + '\n')
