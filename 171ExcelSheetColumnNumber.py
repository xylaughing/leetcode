class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        output = 0
        for i in range(len(columnTitle)):
            output += (ord(columnTitle[len(columnTitle)-i-1]) - 64) * pow(26,i)
        
        return output
