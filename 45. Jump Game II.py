class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        pointer, step = 0, nums[0]
        res = 1
        while step < len(nums)-1:
            pointer, step = step, max([i + nums[i] for i in range(pointer, step+1)])
            res += 1
        return res
