class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        
    
    # turn to math problem
    # return ((len(nums) + 1) * len(nums)) // 2 - sum(nums)
