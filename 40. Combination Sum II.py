class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates, target, [], res)
        return res
        
    def dfs(self, arr, target, path, res):
        if target < 0:
            return
        if target == 0:
            return res.append(path)
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            self.dfs(arr[i+1:], target - arr[i], path + [arr[i]], res)
