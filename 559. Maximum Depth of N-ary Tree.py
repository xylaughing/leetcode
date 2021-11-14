"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        if not root.children: return 1
        #return 1 + max([self.maxDepth(x) for x in root.children])
        temp = 0
        for x in root.children:
            temp = max(temp, self.maxDepth(x))
        return 1 + temp
