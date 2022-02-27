# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(res, node, depth):
            if not node: return
            if depth == len(res):
                res.append(node.val)
            helper(res, node.right, depth+1)
            helper(res, node.left, depth+1)
        
        res = []
        helper(res, root, 0)
        return res
