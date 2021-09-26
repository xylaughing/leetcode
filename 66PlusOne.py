class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        plusone = digits[-1] + 1
        digits[-1] = plusone % 10
        carry = plusone // 10
        i = len(digits) - 2
        while i >= 0 and carry == 1:
            plusone = digits[i] + carry
            carry = plusone // 10
            digits[i] = plusone % 10 
            i -= 1
        if carry == 1:
            digits.insert(0, 1)
            
        return digits
