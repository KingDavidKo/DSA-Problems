# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.recur(root) != -1
    
    def recur(self,root):
        if root is None:
            return 0
        left = self.recur(root.left)
        right = self.recur(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) >=2:
            return -1
        return max(left, right) + 1