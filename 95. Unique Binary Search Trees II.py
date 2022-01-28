# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(left, right):
            if left > right: return [None]
            res = []
            for curNode in range(left, right+1):
                leftTrees = helper(left, curNode-1)
                rightTrees = helper(curNode+1, right)
                
                for lefttree in leftTrees:
                    for righttree in rightTrees:
                        curRoot = TreeNode(curNode)
                        curRoot.left = lefttree
                        curRoot.right = righttree
                        res.append(curRoot)
            return res
                        
        return helper(1, n)
