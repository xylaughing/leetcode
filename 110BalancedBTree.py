# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def maxDepth(node):
            if node is None: return 0
            if node.right is None and node.left is None: return 1
            return 1 + max(maxDepth(node.right), maxDepth(node.left))
        
        if root is None: return True       
        if abs(maxDepth(root.right) - maxDepth(root.left)) > 1:
            return False
        else:
            return self.isBalanced(root.right) and self.isBalanced(root.left)
        
