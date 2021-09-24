class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#        local_max of i is max(local_max of i-1 * Ai, Ai, local_min of i-1 * Ai )
#        local_min of i is min(local_min of i-1 * Ai, Ai, local_max of i-1 *Ai)

        local_max, local_min, global_max = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            temp1 = max(local_max * nums[i], nums[i], local_min * nums[i])
            temp2 = min(local_min * nums[i], nums[i], local_max * nums[i])
            local_max = temp1
            local_min = temp2
            global_max = max(temp1, global_max)
        return global_max
            
