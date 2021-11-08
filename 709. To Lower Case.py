class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        res = ''
        for x in s:
            if 'A' <= x <= 'Z':
               res += chr(ord(x) + 32)
            else:
                res += x
        return res
        """
        return ''.join(chr(ord(x) + 32) if 'A' <= x <= 'Z' else x for x in s)
