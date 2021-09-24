class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l_word = s.split()[-1]
        return len(l_word)
    
    
"""       
        count = 0
        check = True
        for i in range(len(s), 0, -1):
            while check:
                if count == 0 and s[i-1] == ' ':
                    check = True
                    break
                else:
                    if s[i-1] != ' ':
                        count += 1
                        break
                    else:
                        check = False                      
        return count
"""
