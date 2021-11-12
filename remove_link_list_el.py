import json
from itertools import islice
from typing import Optional

# 203. Remove Linked List Elements - Easy
# Given the head of a linked list and an integer val, remove all the nodes
# of the linked list that has Node.val == val, and return the new head.
#
# https://leetcode.com/problems/remove-linked-list-elements/

from _structs_leetcode import ListNode

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val: # delete first nodes with val
            head = head.next
        
        if not head: # check that any nodes exists
            return None

        cur = head        
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head    
    

if __name__ == '__main__':    
    with open('./OUTPUT/IN', 'r') as f_in, open('./OUTPUT/OUT', "w") as f_out:
        while True:
            n_args = 2
            args_raw = [x.rstrip() for x in islice(f_in, n_args)]
            if not args_raw:
                break

            exec = Solution()
            res = exec.removeElements(ListNode.buildFromList(ListNode(), json.loads(args_raw[0])), int(args_raw[1]))    

            f_out.write(json.dumps(res.toList() if res else []) + '\n')
