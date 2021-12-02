class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        """
        dic = {1: 'I', 4:'IV', 5:'V', 9:'IX', 10: 'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        times, res = 0, ''
        while num > 0:
            bit = num % 10
            if bit in [1, 4, 5, 9]:
                res = dic[bit * 10**times] + res
            elif 1< bit < 4:
                res = dic[1 * 10**times] * bit + res
            elif 5 < bit < 9:
                res = dic[5 * 10**times] + dic[1*10**times]*(bit-5) + res
            num = num // 10
            times += 1
        return res
        """
        
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res, i = '', 0
        while num > 0:
            res += (num//nums[i]) * romans[i]
            num = num%nums[i]
            i += 1
        return res
