# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == targetSum:
            return True
        left_match = self.hasPathSum(root.left, targetSum-root.val)
        right_match = self.hasPathSum(root.right, targetSum-root.val)
        return left_match or right_match
        
        
"""       
        # given a BTree, return a array with all pathsum
        def pathsum(root):
            output = []
            if root is None: return [0]
            if root.left is None and root.right is None: return [root.val]
            if root.left is not None:
                output.extend(x+root.val for x in pathsum(root.left))
            if root.right is not None:
                output.extend(x+root.val for x in pathsum(root.right))
            return output

        if root is None: return False
        return targetSum in pathsum(root)
"""
