class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1: return 2**31 - 1
        if (dividend>0 and divisor>0) or (dividend < 0 and divisor < 0):
            neg = 1
        else:
            neg = -1
        dividend, divisor = abs(dividend), abs(divisor)
        
        """
        quotient = 0
        while dividend >= divisor:    
            dividend -= divisor 
            quotient += 1
        return neg * quotient
        """
        quotient, temp = 0, 0
        for i in range(31, -1, -1):
            if (temp + (divisor << i) <= dividend):
                temp += divisor << i;
                quotient |= 1 << i;
        return neg * quotient
