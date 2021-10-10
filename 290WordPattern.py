class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dic = {}
        s = s.split()
        if len(pattern) != len(s): return False
        for i in range(len(pattern)):
            if pattern[i] not in dic.keys():
                if s[i] in dic.values():
                    return False              
                else: dic[pattern[i]] = s[i]
            else:
                if dic[pattern[i]] != s[i]:
                    return False
        return True
