import json

from typing import Optional

#
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# https://leetcode.com/problems/add-two-numbers/
# 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    remember = (l1.val + l2.val) // 10
    r = ListNode(val = (l1.val + l2.val) % 10)
    cur = r
    l1, l2 = l1.next, l2.next
    while l1 or l2 or remember :
        val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + remember
        remember = val // 10
        new = ListNode(val % 10)
        cur.next, cur = new, new
        l1, l2 = (l1 and l1.next), (l2 and l2.next)    

    return r


if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out :
        readen_line_1 = f_in.readline().rstrip()
        readen_line_2 = f_in.readline().rstrip()
        while readen_line_1 and readen_line_2 :
            first = json.loads(readen_line_1)
            second = json.loads(readen_line_2)

            node_line_first = ListNode(first[0])
            prevNode = node_line_first
            for i in range(1, len(first)) :
                curNode = ListNode(first[i])
                prevNode.next = curNode
                prevNode = curNode

            node_line_second = ListNode(second[0])
            prevNode = node_line_second
            for i in range(1, len(second)) :
                curNode = ListNode(second[i])
                prevNode.next = curNode
                prevNode = curNode

            res = addTwoNumbers(node_line_first, node_line_second)

            result = []
            while res :
               result.append(res.val)
               res = res.next

            f_out.write(json.dumps(result) + '\n')
            readen_line_1 = f_in.readline().rstrip()
            readen_line_2 = f_in.readline().rstrip()

