# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        output = TreeNode(nums[len(nums)//2])
        if 1 < len(nums) <= 3:
            output.left = TreeNode(nums[0])
        if len(nums) == 3:
            output.right = TreeNode(nums[2])
        elif len(nums) > 3:
                output.left = self.sortedArrayToBST(nums[0 : len(nums)//2])
                output.right = self.sortedArrayToBST(nums[len(nums)//2 + 1 : len(nums)])
        
        return output
