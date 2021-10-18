class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s: return True
        res = ""
        i, j = 0, 0
        while i < len(t) and j < len(s):
            if t[i] != s[j]: i += 1
            else:
                res += s[j]
                i += 1
                j += 1
        for i in range(len(res)-len(s)+1):
             if list(res[i:i+len(s)]) == list(s): 
                return True
