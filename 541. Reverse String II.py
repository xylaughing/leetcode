class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        for i in range((len(s)//k)+1):
            if i*k+k < len(s):
                temp = s[i*k : i*k+k]
            else: temp = s[i*k : ]
            if i%2== 0:
                res += temp[::-1]
            else:
                res += temp
        return res
