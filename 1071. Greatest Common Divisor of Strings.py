class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if not str1 or not str2:
            return str1 if str1 else str2
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        elif str1[0:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):len(str1)], str2)
        else:
            return ""
