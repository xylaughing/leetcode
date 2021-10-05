class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem = []
        if len(nums) == 1: return nums[0]
        
        for i in range(len(nums)-1):
            if nums[i] not in mem:
                if nums[i] not in nums[i+1:len(nums)]:
                    return nums[i]
                else:
                    mem.append(nums[i])
        return nums[i+1]
