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
        stack = deque([root])
        while stack:
            prev = None
            for _ in range(len(stack)):
                node = stack.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return root
