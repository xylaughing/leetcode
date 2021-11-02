# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes = [root] if root else []
        output, flag = [], True
        while nodes:
            temp = [node.val for node in nodes]
            output.append(temp) if flag else output.append(temp[::-1])
            new = []
            for node in nodes:
                if node.left: new.append(node.left)
                if node.right: new.append(node.right)
            nodes = new
            flag = not flag

        return output
