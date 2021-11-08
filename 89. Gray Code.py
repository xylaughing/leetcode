class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        """
        #given arr, return next level gray code
        def nextGraycode(arr, n):
            res = []
            for i in range(len(arr)):
                if i %2 == 0:
                    res += [arr[i], arr[i]|1<<n]
                else:
                    res += [arr[i]|1<<n, arr[i]]
            return res
        
        res = [0]
        for i in range(n):
            res = nextGraycode(res, i)
            n -= 1
        return res
        """
        res = [0]
        for i in range(n):
            res += [x|1<<i for x in res[::-1]]
        return res
