class Solution(object):
    def helper(self, nums, start, path, output):
        output.append(path)
        for i in range(start, len(nums)):
            self.helper(nums, i+1, [nums[i]]+path, output)    
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """ 
        if not nums: return [[]]
        res = []
        self.helper(nums, 0, [], res)
        return res
