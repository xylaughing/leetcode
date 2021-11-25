# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # given a BTree, return a array with all pathsum
        def pathsum(root):
            rmaxp, rmaxs = float('-inf'), 0            
            lmaxp, lmaxs  = float('-inf'), 0
            if root is None: return (float('-inf'), 0)
            if root.left is None and root.right is None: 
                return (root.val, max(0, root.val))
            if root.left is not None:
                lmaxp, lmaxs = pathsum(root.left)
            if root.right is not None:
                rmaxp, rmaxs = pathsum(root.right)
            return max(lmaxp, rmaxp, lmaxs + root.val + rmaxs), max(0, lmaxs + root.val, rmaxs + root.val)

        return pathsum(root)[0]
