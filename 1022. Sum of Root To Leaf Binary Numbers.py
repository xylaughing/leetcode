# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.paths = []
        self.total = 0
        def helper(node, path):
            if not node.left and not node.right:
                path += str(node.val)
                self.paths.append(path)
                self.total += int(path, 2)            
            if node.left:
                helper(node.left, path+str(node.val))
            if node.right:
                helper(node.right, path+str(node.val))

        helper(root, "")
        return self.total 
