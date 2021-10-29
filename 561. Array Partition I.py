class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums, reverse = True)
        return sum(min(nums[i], nums[i+1]) for i in range(0, len(nums)-1, 2))
