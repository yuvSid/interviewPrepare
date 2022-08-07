import json
from typing import Optional

from _structs_leetcode import ListNode

# 19. Remove Nth Node From End of List - # Medium
# Given the head of a linked list, remove the nth node from 
# the end of the list and return its head.
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = node = head
        pos = 0
        while node:
            if pos - n - 1 >= 0:
                prev = prev.next
            node = node.next
            pos += 1
        
        if n > pos -1: # check that deletes node not first or only one in list
            head = head.next
        else:
            prev.next = prev.next.next

        return head

if __name__ == '__main__':    
    with open('OUTPUT/IN', 'r') as f_in, open('OUTPUT/OUT', "w") as f_out:
        while True:
            list_line = f_in.readline().rstrip()
            target_line = f_in.readline().rstrip()
            if not (list_line and target_line):
                break
            list = ListNode.buildFromList(ListNode(), json.loads(list_line))

            exec = Solution()
            res = exec.removeNthFromEnd(list, int(target_line))    

            f_out.write(json.dumps((res.toList()) if res else []) + '\n')
