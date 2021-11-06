class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1: return True
        def isPalindrom(s):
            mid = len(s) // 2
            return s[0: mid] == s[len(s)-mid:][::-1]
            """
            i, j = 0, len(s)-1
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else: return False
            return True
            """
            
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return isPalindrom(s[i+1:j+1]) or isPalindrom(s[i:j])
        return True
