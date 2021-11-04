# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    min1 = min2 = float('inf')
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dsf(root):
            if not root: return
            if root.val >= self.min2: return
            if self.min1 < root.val < self.min2: 
                self.min2 = root.val
            if self.min1 > root.val: 
                self.min1, self.min2 = root.val, self.min1
            dsf(root.left)
            dsf(root.right)

        dsf(root)
        return -1 if self.min2 == float('inf') else self.min2   
