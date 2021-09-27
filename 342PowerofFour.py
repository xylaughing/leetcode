class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        while n > 0 and count <= 2:
            count += n%4
            n = n // 4
        return count == 1
