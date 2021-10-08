# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def inorder(r):
            if r is None:    return []
            return inorder(r.left) + [r.val] + inorder(r.right)
        
        arr = inorder(root)
        l, h = 0, len(arr)-1
        while l < h:
            if arr[l] + arr[h] == k:
                return True
            if arr[l] + arr[h] > k:
                h -= 1
            else: l += 1
        return False
