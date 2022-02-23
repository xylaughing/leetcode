# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root: return (0, 0)
            left = helper(root.left)
            right = helper(root.right)
            return (left[1] + root.val + right[1], max(left) + max(right))
        
        return max(helper(root))
