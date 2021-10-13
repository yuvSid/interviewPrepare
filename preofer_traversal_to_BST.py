
import json
from typing import Optional
from collections import deque

# 1008. Construct Binary Search Tree from Preorder Traversal - Medium
# Given an array of integers preorder, which represents the preorder 
# traversal of a BST (i.e., binary search tree), construct the tree and return its root.
# It is guaranteed that there is always possible to find a binary search 
# tree with the given requirements for the given test cases.
# A binary search tree is a binary tree where for every node, 
# any descendant of Node.left has a value strictly less than Node.val, 
# and any descendant of Node.right has a value strictly greater than Node.val.
# A preorder traversal of a binary tree displays the value of the node first, 
# then traverses Node.left, then traverses Node.right.
#
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def toList(self) -> list:
        res = []
        to_append = deque([self])
        while len(to_append):
            check = to_append.popleft()            
            if check:
                res.append(check.val)
                to_append.append(check.left)
                to_append.append(check.right)
            else:
                res.append(check) # None vall
        
        for i in range(len(res)-1, 0, -1):
            if res[i]:
                break
        return res[:i+1]
        

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:   
        tree = TreeNode(val = preorder[0])
        for each in preorder[1:]:
            place = tree
            while True:
                if each < place.val:
                    if not place.left:
                        place.left = TreeNode(val = each)
                        break
                    place = place.left
                else:
                    if not place.right:
                        place.right = TreeNode(val = each)
                        break
                    place = place.right

        return tree

# using stack
class SolutionSecond:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:   
        tree = TreeNode(preorder[0])
        stack = [tree]

        for each in preorder[1:]:
            if each < stack[-1].val:
                stack[-1].left = TreeNode(each)
                stack.append(stack[-1].left)
                continue
            while stack and each >= stack[-1].val:
                last = stack.pop()
            last.right = TreeNode(each)
            stack.append(last.right)

        return tree

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            readen_line = f_in.readline().rstrip()
            if not readen_line:
                break
            readen = json.loads(readen_line)

            exec = SolutionSecond()
            res = exec.bstFromPreorder(readen)    

            f_out.write(json.dumps(res.toList()) + '\n')
