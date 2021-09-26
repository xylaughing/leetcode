class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """        
        output = ""
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j>=0:
            if i >= 0:  a = int(num1[i])
            else: a = 0
            if j >= 0:  b = int(num2[j])
            else: b = 0
            carry, temp = divmod(a + b + carry, 10)
            output = repr(temp) + output
            i -= 1
            j -= 1
        if carry > 0:   output = '1' + output
                
        return output
