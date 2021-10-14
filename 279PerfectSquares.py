class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isPerfectSq(num):
            return sqrt(num) == int(sqrt(num))
                                    
        dic = [n] * (n+1)
        dic[0] = 0
        for i in range(1, n+1):
            for s in range(1, int(sqrt(n)) + 1):
                dic[i] = min(dic[i], 1 + dic[i-s*s])
        return dic[n]
