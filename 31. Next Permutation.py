class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # from the end, find the decreasing point
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # if nums are in decreasing order, reverse it
        if i == -1: 
            nums.reverse()
            return
        j = len(nums)-1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        # sorting nums[i+1:] in ascending order
        l, r = i+1, len(nums)-1
        while l < r:
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
