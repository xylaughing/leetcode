class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        """ Faster       
        if n == 0: return False        
        if n == 1: return True
        for x in [2,3,5]:
            if n / float(x) == n // x:
                return self.isUgly(n//x)
        return False
        
        """ 
        
        if n <= 0: return False;
        while n % 2 == 0: n /= 2
        while n % 3 == 0: n /= 3
        while n % 5 == 0: n /= 5
        return n == 1;
        
