# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        def pathsum(root):
            res = []
            if not root: return ['']
            if root.left is None and root.right is None:
                return [str(root.val)]
            if root.left:
                res.extend(str(root.val) + x for x in pathsum(root.left))
            if root.right:
                res.extend(str(root.val) + x for x in pathsum(root.right))
            return res

        return sum([int(x) for x in pathsum(root)])
        """
        def helper(root, val):
            if not root: return 0
            if not root.left and not root.right:
                return val*10 + root.val
            return helper(root.left, val *10 + root.val) + helper(root.right, val*10 + root.val)
        
        return helper(root, 0)
