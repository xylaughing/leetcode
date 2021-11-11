class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        """
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return i
        """
        
        l, r = 0, len(arr)-1
        while l < r:
            mid = (l + r) / 2
            if arr[mid] > arr[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l
        
