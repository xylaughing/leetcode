class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        minInd = len(s)
        ct = Counter(s)
        for x in ct:
            if ct[x] == 1:
                minInd = min(s.index(x), minInd)
        
        if minInd == len(s): return -1
        else: return minInd
        
        
        """ Slower but why
        for i in range(len(s)):
            if ct[s[i]] == 1:
                return i
        return -1
        """
