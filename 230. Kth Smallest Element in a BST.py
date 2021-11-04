# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        """
        self.mins = [float('inf')] * k
        def dfs(root):
            if not root: return
            if root.val > self.mins[-1]: return
            else:
                self.mins = sorted([root.val]+self.mins[0:k-1])
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return self.mins[-1]
        """
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            k -= 1
            root = stack.pop()
            if k == 0: return root.val
            else:
                root = root.right
        
        """
        def inorder(root):
            if not root: return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        return inorder(root)[k-1]
        """
