class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        if num == 0: return '0'
        if num < 0: num += 2**32
        while num > 0:
            dig = num % 16
            if dig >= 10: dig = chr(dig+87)
            res = str(dig) + res
            num = num // 16
        
        return res
