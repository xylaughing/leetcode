class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j, count = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] > s[j]: j += 1
            else: 
                i, j, count = i+1, j+1, count+1
        return count
        
