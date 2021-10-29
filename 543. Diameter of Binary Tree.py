# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxs = 0
        def depth(node):
            if node is None: return 0
            l, r = depth(node.left), depth(node.right)
            self.maxs = max(self.maxs, l+r)
            return max(l, r) + 1
          
        depth(root)
        return self.maxs
            
