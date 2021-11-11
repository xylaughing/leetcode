class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        if len(s) < 3: return []
        lastend = -1
        res = []
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                if (i-lastend) > 2: 
                    res.append([lastend + 1, i]) 
                lastend = i
        if s[-1] == s[-2] and (len(s)-1-lastend) > 2:
            res.append([lastend+1, len(s)-1])
        return res
