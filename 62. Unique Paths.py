class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
    
        """
        if m < n:
            m, n = n, m
        dp = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                dp[j] += dp[j-1]
        return dp[m-1]
        
        """
        # Math: total m+n-2 moves, including m-1 down moves and n-1 right moves. So C(m+n-1, m-1) = C(m+n-2, n-1)
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)
        """
        
