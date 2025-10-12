# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sums = ListNode()
        first = sums
        while l1 or l2:
            if l1 and l2:
                if l1.val + l2.val + sums.val >= 10:
                    sums.next = ListNode(1)
                sums.val = (l1.val + l2.val + sums.val) % 10  
                l1 = l1.next
                l2 = l2.next
            elif l1:
                if l1.val + sums.val >= 10:
                    sums.next = ListNode(1)
                sums.val = (l1.val + sums.val) % 10  
                l1 = l1.next
            else:
                if l2.val + sums.val >= 10:
                    sums.next = ListNode(1)
                sums.val = (l2.val + sums.val) % 10  
                l2 = l2.next
            if l1 or l2:
                if not sums.next:
                    sums.next = ListNode(0)
                sums = sums.next
        return first

        