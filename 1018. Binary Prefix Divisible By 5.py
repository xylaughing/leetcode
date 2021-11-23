class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        res = [False] * len(nums)
        x = 0
        for i in range(len(nums)):
            x = x * 2 + nums[i]
            if x % 5 == 0:
                res[i] = True
        return res
