class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bit = n & 1
        while n > 0:
            n = n >> 1
            if abs(bit - n&1) != 1:
                return False
            bit = n&1
        return True
