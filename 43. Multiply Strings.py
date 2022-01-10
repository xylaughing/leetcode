class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def xdigit(num, dig):
            if dig == 0: return "0"
            carry = 0
            res = ""
            for i in range(len(num)-1, -1, -1):
                carry, temp = divmod(int(num[i]) * dig + carry, 10)
                res = str(temp) + res
            return  str(carry) + res if carry != 0 else res
        
        def addstring(str1, str2):
            i, j = len(str1)-1, len(str2)-1
            output, carry = "", 0
            while i >= 0 or j >= 0:
                if i < 0: a = 0
                else:
                    a = int(str1[i])
                if j < 0: b = 0
                else:
                    b = int(str2[j])
                carry, temp = divmod(a+b+carry, 10)
                output = str(temp) + output
                i, j = i-1, j-1
            return "1" + output if carry > 0 else output
        
        if num1 == "0" or num2 == "0": return "0"
        res = ""
        for i in range(len(num2)-1, -1, -1):
            temp = xdigit(num1, int(num2[i]))
            temp += "0" * (len(num2)-1-i)
            res = addstring(res, temp)
            print(i, temp, res)
        return res
