class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0: return True if nums[0] > 0 else False
        pointer, step = 0, nums[0]
        while step < len(nums)-1:
            prev = step
            pointer, step = step, max([i+ nums[i] for i in range(pointer, step+1)])
            if step == prev: return False
        return True
        
