"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right and node.left:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                stack.append(node.right)
                stack.append(node.left)
        return root
