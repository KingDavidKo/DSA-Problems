# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        elem = []

        for i in lists:
            curr = i
            while (curr):
                elem.append(curr.val)
                curr = curr.next
        elem.sort()
        if (len(elem) == 0):
            return None
        output = ListNode()
        curr = output
        temp = None
        i = 0
        for i in range(len(elem)-1):
            curr.val = elem[i]
            curr.next = ListNode()
            curr = curr.next
        curr.val = elem[-1]
        return output

        