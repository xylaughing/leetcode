class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # local max of index i = max(Ai, Ai + local max of index (n-1))

        localmax = 0
        globalmax = float ('-inf')
        for i in range(len(nums)):
            localmax = max(nums[i], nums[i] + localmax)
            if localmax > globalmax:
                globalmax  = localmax
                                    
        return globalmax
