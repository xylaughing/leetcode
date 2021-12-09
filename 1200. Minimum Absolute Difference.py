class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        res, mindiff = [], float('inf')
        arr = sorted(arr)
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < mindiff:
                res = [[arr[i], arr[i+1]]]
                mindiff = arr[i+1] - arr[i]
            elif arr[i+1] - arr[i] == mindiff:
                res.append([arr[i], arr[i+1]])
        return res
