class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) < 3: return s
        res = ""
        for i in range(len(s)-2):
            if s[i] == s[i+1] == s[i+2]:
                continue
            else:
                res += s[i]
        return res + s[-2] + s[-1]
