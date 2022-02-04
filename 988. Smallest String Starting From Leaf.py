# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def helper(root, res):
            if not root: return res
            res = chr(root.val + 97) + res
            if not root.left and not root.right:
                return res
            if not root.left:
                return helper(root.right, res)
            if not root.right:
                return helper(root.left, res)
            return min(helper(root.left, res), helper(root.right, res))

        return helper(root, "")
