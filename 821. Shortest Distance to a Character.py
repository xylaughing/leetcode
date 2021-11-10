class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        res = [0] * len(s)
        # find the index of c
        ind_c = [i for i in range(len(s)) if s[i] == c]
        for i in range(len(s)):
            res[i] = min([abs(x-i) for x in ind_c])
        return res
