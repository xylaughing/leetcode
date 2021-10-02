# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # preorder with Null
        def preorder(root):
            if root is None: return []
            if root.left is None: return [root.val] + ['Null'] + preorder(root.right)
            if root.right is None: return [root.val] + preorder(root.left) + ['Null']
            
            return [root.val] + preorder(root.left) + preorder(root.right)
        
        pArr = preorder(p)
        qArr = preorder(q)
        return pArr == qArr
