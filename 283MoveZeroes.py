class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        z_p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[z_p]
                nums[z_p] = nums[i]
                nums[i] = temp
                z_p += 1
        
        return nums[:z_p]
