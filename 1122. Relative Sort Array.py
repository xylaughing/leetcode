class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res = []
        ct = Counter(arr1)
        arr2 += sorted(set(arr1) - set(arr2))
        for x in arr2:
            res += [x] * ct[x]
        return res
