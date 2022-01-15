class Solution(object):
    def dfs(self, nums, path, output):
        output.append(path)
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                self.dfs(nums[i+1:], path+[nums[i]], output)
                  
        
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums), [], res)
        return res
