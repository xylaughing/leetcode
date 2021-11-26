class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for x in s:
            if not res or res[-1] != x:
                res.append(x)
            elif res[-1] == x:
                res.pop()
        return ''.join(res)
