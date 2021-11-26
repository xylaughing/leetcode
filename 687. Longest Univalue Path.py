# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.LUP = 0
        def path(node):
            if not node: return (0, 0)
            Llongestside, Rlongestside = 0, 0
            left, right = 0, 0
            if node.left is not None:
                Llongestside = path(node.left)
                if node.left.val == node.val:
                    left = Llongestside + 1
            if node.right is not None:
                Rlongestside = path(node.right)
                if node.right.val == node.val:
                    right = Rlongestside + 1
            self.LUP = max(self.LUP, left+right)
            return max(left, right)
        
        path(root)
        return self.LUP
        
