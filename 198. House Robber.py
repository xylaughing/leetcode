class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        if len(nums) == 1: return nums[0]               
        if len(nums) == 2: return max(nums)
        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))               
        """
        """
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-1],  (nums[i-1] + dp[i-2]))
        return dp[-1]
        """
        
        prev, cur = 0, nums[0]
        for i in range(2, len(nums)+1):
            temp = max(cur, nums[i-1] + prev)
            prev, cur = cur, temp
        return cur
