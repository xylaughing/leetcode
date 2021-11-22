class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        def isPalindrome(s):
            return s == s[::-1]
        
        res = ""
        for i in range(len(s)):
            j = len(s) - 1
            while j >= i + len(res):
                while s[i] != s[j]:
                    j -= 1
                if isPalindrome(s[i:j+1]):
                    if j + 1 - i > len(res):
                        res = s[i:j+1]
                        break
                else:
                    j -= 1
        return res
        """
        maxlen, maxind = 1, 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j: dp[i][j] = True
                elif s[i] == s[j]:
                    if j-i <= 2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if (j - i + 1) > maxlen:
                            maxlen, maxind = j-i+1, i
        return s[maxind : maxind + maxlen]
                        
