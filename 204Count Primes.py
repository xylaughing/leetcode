class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return 0
        
        # create strike list for the input range, initializing all indices to 1.
        strikes = [1] * n
        # we know that 0 and 1 are not prime
        strikes[0], strikes[1] = 0, 0
        
        for i in range(2, int(sqrt(n))+1):
            if  strikes[i] != 0:   
                strikes[i*i: n: i] = [0] * len(strikes[i*i: n: i])
        return sum(strikes)
        
        
        """
        def isPrime(num):
            if num in [0,1]: return False
            for i in range(2, int(sqrt(num)) + 1):
                if num %i == 0:
                    return False
            return True        
        """
