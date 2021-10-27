class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """     
        """
        start, maxs, temp = s[0], 0, 1
        for i in range(1, len(s)):
            if s[i] == start:
                temp += 1
            else:
                if maxs <= temp: 
                    maxs = temp
                temp, start = 1, s[i]
        return max(maxs, temp)
        """
        
        return max(len(list(j)) for _, j in (groupby(s)))
