class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        n, res = abs(num), ''
        if num == 0: return '0'
        while n > 0:
            res = str(n%7) + res
            n = n / 7
        return '-' * (num<0) + res
