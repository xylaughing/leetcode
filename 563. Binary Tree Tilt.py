# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sums = 0
        def dp(node):
            if node is None: return 0
            L, R = dp(node.left), dp(node.right)
            self.sums += abs(L-R)
            return L + R + node.val  
        
        dp(root)
        return self.sums
