class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """        
        if len(nums) == 1: return [nums]
        n = len(nums)
        temp = self.permute(nums[0:n-1])
        add = nums[-1]
        res = []
        for x in temp:
            i = 0
            res.append([add]+x)
            while i < len(x):
                res.append(x[0:i+1]+[add]+x[i+1:])
                i += 1
        return res
        """
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path+[nums[i]], res)   
                
