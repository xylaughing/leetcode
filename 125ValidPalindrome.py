class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        strList = list(re.sub("[^a-zA-Z0-9]","", s.lower()))
        i, j = 0, len(strList)-1
        mid = (i + j) //2
        while i <= mid and j >=mid and i < j:
            if strList[i] != strList[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
    
    
    
"""
isalnum() True if all characters in the string are alphanumeric
"""
            
