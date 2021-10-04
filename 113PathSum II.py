# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        def path(node, targetSum, curpath):
            if node is None: return 0
            if node.left is None and node.right is None and node.val == targetSum:
                curpath.append(node.val)
                output.append(curpath)
            if node.left is not None:
                path(node.left, targetSum - node.val, curpath + [node.val])
            if node.right is not None:
                path(node.right, targetSum - node.val, curpath + [node.val])
        
        output = []
        path(root, targetSum, [])
        return output
