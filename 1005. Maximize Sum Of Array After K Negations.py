class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        i, lastneg = 0, float('inf')
        while i < k and i < len(nums) and nums[i] < 0:
                nums[i] = -nums[i]
                i += 1
        if k-i > 0 and (k-i)%2 == 1:
            return sum(nums) - 2 * min(nums)
        else:
            return sum(nums)
