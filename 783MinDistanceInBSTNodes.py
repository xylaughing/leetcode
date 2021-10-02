# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(root):
            if root is None: return []            
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        arr = inorder(root)
        for i in range(len(arr)-1):
            temp = arr[i+1] - arr[i]
            if temp < 0: arr[i] = - temp
            else: arr[i] = temp
        
        return min(arr[0:len(arr)-1])
            
