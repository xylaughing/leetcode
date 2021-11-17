# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(root):
            if not root: return []
            if not root.left and not root.right:
                return [root.val]
            return inorder(root.left) + [root.val] + inorder(root.right)
    
        res = inorder(root)
        head = temp = TreeNode(res[0])
        for i in range(1,len(res)):
            temp.right = TreeNode(res[i])
            temp = temp.right
        return head
        
