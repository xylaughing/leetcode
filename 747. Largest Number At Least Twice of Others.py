class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        maxind = 0
        maxval = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > maxval:
                maxval = nums[i]
                maxind = i
        for i in range(len(nums)):
            if nums[i] != maxval:
                if maxval < nums[i]*2:
                    return -1
        return maxind
        """
        max1 = max2 = float('-inf')
        maxind = 0
        for ind, num in enumerate(nums):
            if num > max1:
                max1, max2 = num, max1
                maxind = ind
            elif num > max2:
                max2 = num
        return maxind if max1 >= 2*max2 else -1
