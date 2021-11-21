class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) ==  1: return False
        if arr[0] >= arr[1] or arr[-1] >= arr[-2]: return False
        res = []
        for i in range(1, len(arr)-1):
            if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
                res.append(arr[i])
        return True if len(res)==1 else False
