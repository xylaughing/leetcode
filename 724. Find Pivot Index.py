class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = sum(nums)
        if nums[0] == sums: return 0
        dp = [nums[0]] * len(nums)        
        for i in range(len(nums)-1):
            dp[i+1] = dp[i] + nums[i+1]
            if dp[i+1] == sums - dp[i]:
                return i+1 
        return -1
