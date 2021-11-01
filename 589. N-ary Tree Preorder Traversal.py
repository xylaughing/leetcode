"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def helper(root, output):
            if root is None: return
            output.append(root.val)
            if root.children is not None:
                for x in root.children:
                    helper(x, output)
        
        helper(root, res)
        return res
        
