# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def __init__(self):
        self.length = 0
        self.n1 = 1
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            head.next = None
            self.length += 1
        else:
            head.next = self.removeNthFromEnd(head.next, n)
            self.length += 1
        
        if self.n1 != n:
            self.n1 += 1
            return head
        else:
            self.n1 += 1
            return head.next
        

        
        

        


