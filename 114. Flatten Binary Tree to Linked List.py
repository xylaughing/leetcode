# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
   
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return
        left = root.left
        right = root.right
        root.left = None
        
        self.flatten(left)
        self.flatten(right)
        root.right = left
        root.left = None
        
        end = root
        while end.right: end = end.right
        end.right = right
