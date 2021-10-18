# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        L, R = 0, 0
        if root.left is None and root.right is None: return 0
        
        if root.left is not None:
            L = self.sumOfLeftLeaves(root.left)
            if L == 0 and root.left.right is None and root.left.left is None:
                L = root.left.val
            
        if root.right is not None:
            R = self.sumOfLeftLeaves(root.right)
        
        return L + R
