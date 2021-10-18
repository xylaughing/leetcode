class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ct = Counter(s)
        res, asy = 0, 0
        for x in ct.keys():
            if ct[x] % 2 == 1: asy = 1
            res += ct[x] // 2
        return res*2+ asy
