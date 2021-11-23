class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        if n == 0: return 1
        res, i = 0, 0
        while n > 0:
            if n & 1 == 0:
                res += (1- n & 1) * 2**i
            i += 1
            n = n >>1
        return res
        
        """
        x = 1
        while x < n: x = x*2 + 1
        return x - n 
        """
