class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high, mid = 0, num, 0
        while low <= high:
            mid = (low + high) // 2
            if (mid * mid) == num:
                return True
            else:
                if (mid * mid) > num:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return False
