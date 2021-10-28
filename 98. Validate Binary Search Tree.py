# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dp(node, floor, ceiling):
            if not node: return True
            if node.val <= floor or node.val >= ceiling: 
                return False
            return dp(node.left, floor, node.val) and dp(node.right, node.val, ceiling)
        
        return dp(root, float('-inf'), float('inf'))
