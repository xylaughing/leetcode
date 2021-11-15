class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        one, lastone, maxs = 32, 32, 0
        for i in range(32):
            if n&1 == 1:
                one, lastone = i, one
                maxs = max(maxs, one-lastone)
            n = n >> 1
            if n == 0: break
        return maxs
