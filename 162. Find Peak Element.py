class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 3: return nums.index(max(nums))
        l, r = 1, len(nums)-1
        while l < r:
            i = (l + r) / 2
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            elif nums[i-1] < nums[i] < nums[i+1]:
                l = i + 1
            else:
                r = i
        return l-1 if l==1 else l
