class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1: return 0
        maxV, minV = max(nums), min(nums)
        if maxV - minV > 2*k:
            return maxV - minV - 2*k
        else:
            return 0
