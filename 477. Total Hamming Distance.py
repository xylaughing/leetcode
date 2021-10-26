class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = [0] * 32
        res = 0
        for num in nums:
            i = 0
            while num:
                if num&1 == 1: ones[i] += 1
                num = num>>1
                i += 1
        for x in ones:
            res += x * (len(nums)-x)

        return res 
