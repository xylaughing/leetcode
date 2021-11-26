class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x, y = max(nums), min(nums)
        while y != 0:
            (x, y) = (y, x % y)
        return x
