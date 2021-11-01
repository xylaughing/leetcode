"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        nodes = [root] if root else[]
        output = []
        while nodes:
            output.append([x.val for x in nodes])
            nodes = [child for node in nodes for child in node.children if child]
        return output
