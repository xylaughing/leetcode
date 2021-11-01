"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        def helper(root, output):
            if root is None: return
            if root.children is not None:
                for x in root.children:
                    helper(x, output)
            output.append(root.val)
    
        res = []
        helper(root, res)
        return res
