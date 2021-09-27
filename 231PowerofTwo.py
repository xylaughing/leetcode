class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        if n < 0: return False
        while n != 0:
            count += n%2
            n = n // 2
        return count == 1
       
        
