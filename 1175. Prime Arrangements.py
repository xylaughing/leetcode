class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isPrime(n) :
            # Corner cases
            if (n <= 1) : return False
            if (n <= 3) : return True
            # This is checked so that we can skip middle five numbers in below loop
            if (n % 2 == 0 or n % 3 == 0) :
                return False
            i = 5
            while(i * i <= n) :
                if (n % i == 0 or n % (i + 2) == 0) :
                    return False
                i = i + 6
            return True
        
        prime = 0
        for i in range(1,n+1):
            if isPrime(i):
                prime += 1
        res = 1
        for i in range(2, prime+1):
            res = res * i
        for j in range(2, n-prime+1):
            res = res * j
        return res % (10**9 + 7)
            
