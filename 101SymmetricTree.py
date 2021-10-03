# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def lr_preorder(Tnode):
            if Tnode is None: return []
            if Tnode.left is None and Tnode.right is not None: 
                return [Tnode.val] + [0] + lr_preorder(Tnode.right)
            return [Tnode.val] + lr_preorder(Tnode.left) + lr_preorder(Tnode.right)
        
        def rl_preorder(Tnode):
            if Tnode is None: return []
            if Tnode.right is None and Tnode.left is not None: 
                return [Tnode.val] + [0] + rl_preorder(Tnode.left)
            return [Tnode.val] + rl_preorder(Tnode.right) + rl_preorder(Tnode.left)
        
        return lr_preorder(root.left) == rl_preorder(root.right)
