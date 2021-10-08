class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        output = ""
        while columnNumber:
            output = chr((columnNumber -1)%26 + 65) + output
            columnNumber = (columnNumber -1) // 26
        return output
            
