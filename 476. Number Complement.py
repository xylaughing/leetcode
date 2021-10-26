class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """        
        """
        res = ''
        while num > 0:
            res = str(abs(num%2-1)) + res
            num = num//2
     
        return int(res, 2)
        """
        
        # num XOR 1 = bit flip
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num
