class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        while n > 0 and count <= 2:
            count += n % 3
            n = n // 3
        
        return count == 1
