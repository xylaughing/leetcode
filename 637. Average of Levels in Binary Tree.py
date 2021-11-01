# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nodes = [root] if root else []
        output = []
        while nodes:
            output.append(sum([node.val for node in nodes]) / float(len(nodes)))
            new = []
            for node in nodes:
                if node.left: new.append(node.left)
                if node.right: new.append(node.right)
            nodes = new
        return output
