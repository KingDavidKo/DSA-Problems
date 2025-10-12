# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        mydict = {}
        self.recursive(root, 0, 0, mydict)
        for col in sorted(mydict.keys()):
            sorted_nodes = sorted(mydict[col], key=lambda x: (x[0], x[1]))
            output.append([val for _, val in sorted_nodes])
        return output

        
    def recursive(self, root, row, col, mydict):
        if (root is None):
            return
        self.recursive(root.left, row + 1, col - 1, mydict)
        if col in mydict:
            mydict[col].append((row, root.val))
        else:
            mydict[col] = [(row, root.val)]        
        self.recursive(root.right, row + 1, col + 1, mydict)