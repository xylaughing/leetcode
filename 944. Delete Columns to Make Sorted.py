class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res = 0
        arr = [[strs[i][j] for i in range(len(strs))] for j in range(len(strs[0]))]
        """
        for i in range(len(arr)):
            for j in range(len(arr[i])-1):
                if arr[i][j+1] < arr[i][j]:
                    res += 1
                    break
        return res
        """
        return sum([any(arr[i][j+1] < arr[i][j] for j in range(len(arr[0])-1)) for i in range(len(arr))])
