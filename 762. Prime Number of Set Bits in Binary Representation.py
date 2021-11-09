class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def numofBits(num):
            res = 0
            for i in range(20):
                res += num & 1
                num = num>>1
            return res
        res = 0
        primeset = [2, 3, 5, 7, 11, 13, 17, 19]
        for num in range(left, right+1): 
            if numofBits(num) in primeset: 
                res += 1
        return res
