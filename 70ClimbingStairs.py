class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """  

        def climbStairsMem(n, mem={}):
            if n <= 2: return n
            if n in mem: return mem[n]
            mem[n] = climbStairsMem(n-1, mem) + climbStairsMem(n-2, mem)
            return mem[n]
        
        return climbStairsMem(n, mem={})
    
