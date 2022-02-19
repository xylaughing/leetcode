class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        for i in range(len(s)-9):
            if dic.has_key(s[i:i+10]):
                dic[s[i:i+10]] += 1
            else:
                dic[s[i:i+10]] = 1
        return [x for x in dic.keys() if dic[x] > 1]
