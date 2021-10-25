class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """  
        res = 0

        x = x ^ y
        while x:
            x = x & (x-1)
            res += 1
        return res
        """
        while x != y:
            if x&1 != y&1: res += 1
            x >>= 1
            y >>= 1
        return res
        """ 
