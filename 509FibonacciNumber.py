class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """        
        mem = [0, 1]
        if n <= 1: return n    
        for i in range(2, n+1):
            mem.append(mem[i-1] + mem[i -2])
        return mem[n]
