# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 0
        llist = {}
        curr = head
        while True:
            if curr is None:
                return False
            if curr in llist:
                return True
            llist[curr] = 0
            curr = curr.next

        