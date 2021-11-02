# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes = [root] if root else []
        output = []
        while nodes:
            output.append([node.val for node in nodes])
            temp = []
            for node in nodes:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            nodes = temp
        return output