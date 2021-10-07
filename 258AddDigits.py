class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        """
        def helper(n):
            output = 0
            while n > 0:
                output += n%10
                n = n//10
            return output
        
        if num < 10: return num
        while helper(num) >= 10:
            num = helper(num)
        return helper(num)                
        """
        if num == 0: return 0
        if num%9 == 0: return 9
        else: return num%9
