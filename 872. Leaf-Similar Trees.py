# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def getLeaves(root, leaves = []):
            if not root: return 
            if not root.left and not root.right:
                leaves.append(root.val)
            getLeaves(root.left, leaves)
            getLeaves(root.right, leaves)
        
        res1, res2 = [],[] 
        getLeaves(root1, res1)
        getLeaves(root2, res2)
        return True if res1 == res2 else False
