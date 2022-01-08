class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ct = Counter(arr).values()
        return True if len(Counter(ct)) == len(ct) else False
