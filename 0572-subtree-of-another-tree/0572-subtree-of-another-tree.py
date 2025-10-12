# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        # find root:
        if root is None:
            return False
        if (root.val == subRoot.val):
            
            if self.comparer(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
                    
            
             
        
    def comparer(self, tree1, tree2):
        if (tree1 is None and tree2 is None):
            return True
        if (tree1 is None or tree2 is None):
            return False
        if (tree1.val != tree2.val):
            return False
        return True and self.comparer(tree1.left, tree2.left) and self.comparer(tree1.right, tree2.right)

        