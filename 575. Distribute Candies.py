class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        """
        ct = Counter(candyType)
        return  min(len(ct.keys()), len(candyType)//2)        
        """
        return min(len(candyType)//2, len(set(candyType)))
