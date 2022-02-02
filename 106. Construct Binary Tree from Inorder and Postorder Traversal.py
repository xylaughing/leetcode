# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if postorder:
            rootval = postorder.pop()
            index_in = inorder.index(rootval)
            root = TreeNode(rootval)
            root.left = self.buildTree(inorder[0:index_in], postorder[0:index_in])
            root.right = self.buildTree(inorder[index_in+1:], postorder[index_in:])
            return root
