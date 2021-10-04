# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        output = []        
        if root is None: return []
        if root.left is None and root.right is None: 
            return [str(root.val)]
        
        if root.left is not None:   
            output.extend([str(root.val) + "->" + x for x in self.binaryTreePaths(root.left)])        
        if root.right is not None:
            output.extend([str(root.val) + "->" + x for x in self.binaryTreePaths(root.right)])
            
        return output
