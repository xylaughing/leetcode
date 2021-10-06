class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if s == "": return t
        if t == "": return s
        return list((Counter(t)-Counter(s)).keys())[0]
