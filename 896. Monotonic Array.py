class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        larger, smaller = False, False
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                larger = True
            elif nums[i] < nums[i-1]:
                smaller = True
            if larger and smaller:
                return False
        return True
