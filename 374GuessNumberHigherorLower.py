# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def getinRange(l, h):
            if l > h:
                return l
            else:
                mid = (l + h) // 2
                if guess(mid) == 0:
                    return mid
                else:
                    if guess(mid) == 1:
                        return getinRange(mid+1, h)
                    else:
                        return getinRange(l, mid-1)
        return getinRange(0, n)
