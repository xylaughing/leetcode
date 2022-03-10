class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        output = []
        self.helper(k, n, [], output)
        return output
    
    def helper(self, k, n, path, output):
        if k < 0 or n < 0:
            return
        elif k == 0 and n == 0:
            output.append(path)
        start = path[-1] + 1 if path else 1
        for i in range(start, 10):
            self.helper(k-1, n-i, path+[i], output)    
