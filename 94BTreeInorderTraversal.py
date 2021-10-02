# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        buff, output = [], []
        node = root
        while node or buff:
            while node:
                buff.append(node)
                node = node.left
            temp = buff.pop()
            output.append(temp.val)
            node = temp.right
        return output
        
        
"""
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
