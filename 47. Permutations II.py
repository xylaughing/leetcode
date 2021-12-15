class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res        
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        seen = []
        for i in range(len(nums)):
            if nums[i] not in seen:
                self.dfs(nums[:i]+nums[i+1:], path + [nums[i]], res)
                seen.append(nums[i])
