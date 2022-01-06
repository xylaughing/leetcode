class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        """
        digits = str(num)
        res, changed = 0, False
        for i in range(len(digits)):
            if digits[i] == "6" and changed == False:
                res = res * 10 + 9
                changed = True
            else:
                res = res * 10 + int(digits[i])
        return res
        """
        digits = list(str(num))
        for i in range(len(digits)):
            if digits[i] == '6':
                digits[i] = '9'
                break
        return sum(int(digits[i]) * (10 **(len(digits)-1-i)) for i in range(len(digits)))
