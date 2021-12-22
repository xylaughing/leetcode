class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        fr, lr, fc, lc = 0, n-1, 0, n-1
        num = 1
        res = [[0]*n for i in range(n)]
        while fr < lr and fc < lc:
            for i in range(fc, lr):
                res[fr][i] = num
                num += 1
            for i in range(fr, lr):
                res[i][lc] = num
                num += 1
            for i in range(lc, fc, -1):
                res[lr][i] = num
                num += 1
            for i in range(lr, fr, -1):
                res[i][fc] = num
                num += 1
            fr, lr, fc, lc = fr+1, lr-1, fc+1, lc-1
        if fr == lr: res[fr][fc] = num
        return res
            
