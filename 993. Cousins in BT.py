# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        #given a node, return parent and depth
        def pd(node, parent, depth):
            if node and len(res)<2: 
                if node.val == x or node.val == y:
                    return res.append([parent, depth])
                else:
                    pd(node.left, node, depth+1) 
                    pd(node.right, node, depth+1)

        res = []
        pd(root, None, 0)
        if len(res) < 2: return False
        return res[0][0] != res[1][0] and res[0][1] == res[1][1]
        
