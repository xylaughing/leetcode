class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        low = 0
        high = x
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            if (mid * mid) == x:
                return mid
            else:
                if (mid * mid) > x:
                    high = mid - 1
                else:
                    low = mid + 1
            print("low = ", low )
        if low * low > x:
            return low - 1
        else:
            return low
