class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        i = 0
        while n > i:
            i += 1
            n = n - i
        return i
        
        """
        # faster, turn to math problem, x = (-b + sqrt(b**2- 4ac)) / 2a
        return int(sqrt(1 + 4*(2*n)) / 2 - 0.5)
