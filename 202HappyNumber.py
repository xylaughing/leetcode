class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(num):
            output = 0
            while num >= 1:
                output += pow(num%10, 2)
                num = num // 10
            return output
        
        dic = {}
        if n ==1: return True
        while n != 1:
            if n in dic.keys():
                return False
            else:
                dic[n] = 1
                n = helper(n)
        return True
