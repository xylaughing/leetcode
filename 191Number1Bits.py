class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        """ Option 1
        result = 0
        while n != 0:
            result += n%2 
            n = n // 2
        return result
        """
        
        # Option 2
        res = 0
        for i in range(32):
            res += n&1
            n >>= 1
        return res
