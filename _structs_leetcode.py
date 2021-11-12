from __future__ import annotations

# Realisation of custom structs that are needed in leetcode problems 

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def buildFromList(self, raw: list) -> TreeNode:
        if not raw:
            return None
        
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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def buildFromList(self, raw: list) -> ListNode:
        if not raw:
            return None
        
        self.val = raw[0]
        node = self
        
        for num in raw[1:]:
            node.next = ListNode(num)
            node = node.next
        return self

    def toList(self) -> list:
        if not self:
            return []

        res = [self.val]
        node = self
        while node := node.next:
            res.append(node.val)
        return res
