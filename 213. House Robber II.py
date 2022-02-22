class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(arr):
            if not arr: return 0
            prev, cur = 0, arr[0]
            for i in range(1, len(arr)):
                temp = max(cur, arr[i] + prev)
                prev, cur = cur, temp
            return cur
        
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        return max(nums[0] + helper(nums[2:len(nums)-1]), helper(nums[1:]))
