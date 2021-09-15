class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        romandict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        prev_value = result = 0
        for i in range(len(s)-1, -1, -1):
            cur_value = romandict[s[i]]
            if cur_value < prev_value:
                result -= cur_value
            else:
                result += cur_value
            prev_value = cur_value
        
        return result
