class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        ct = Counter(candyType)
        t, n = len(ct.keys()), len(candyType) / 2
        return  n if n < t else t
