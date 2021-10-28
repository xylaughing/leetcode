# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        def dp(node):
            if node.val not in dic.keys():
                dic[node.val] = 1
            else:
                dic[node.val] += 1
            if node.left is not None: dp(node.left)
            if node.right is not None: dp(node.right)
             
        dic, maxs = {}, 0
        dp(root)
        maxs = max(dic.values())
        return [x for x, y in dic.items() if y == maxs]
        """
        # counter faster than dict
        ct = collections.Counter()
        def dp(node):
            if node:
                ct[node.val] += 1
                dp(node.left)
                dp(node.right)
                
        dp(root)
        maxs = max(ct.itervalues())
        return [x for x, y in ct.items() if y == maxs]
