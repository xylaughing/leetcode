# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            rootval = preorder.pop(0)
            index_inorder = inorder.index(rootval)
            root = TreeNode(rootval)
            root.left = self.buildTree(preorder, inorder[0:index_inorder])
            root.right = self.buildTree(preorder, inorder[index_inorder+1:])
            return root
