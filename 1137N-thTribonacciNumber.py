class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        def trib_mem(n, mem={}):
            if n <= 1: return n
            if n == 2: return 1
            if n in mem: return mem[n]
            mem[n] = trib_mem(n-1, mem) + trib_mem(n-2, mem) + trib_mem(n-3, mem)
            return mem[n]
        
        return trib_mem(n, mem={})
