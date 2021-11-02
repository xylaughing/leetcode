class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == k: return sum(nums) / float(k)
        maxs = pre = sum(nums[0:k]) 
        for i in range(len(nums)-k):
            pre = pre - nums[i] + nums[i+k]            
            if nums[i+k]-nums[i] > 0:
                maxs = max(maxs, pre)            
        return maxs / float(k)
