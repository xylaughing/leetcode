class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        for num in nums:
            if num-1 not in nums:
                temp = num + 1
                while temp in nums:
                    temp += 1
                res = max(res, temp - num)
        return res
