class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs(candidates, target, [], self.res)
        return self.res
    
    def dfs(self, arr, target, path, res):
        if target < 0: 
            return
        if target == 0:
            return res.append(path)
        for i in range(len(arr)):
            self.dfs(arr[i:], target-arr[i], path+[arr[i]], res)
