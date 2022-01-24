class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] += 2 * dp[i-1]
            for j in range(1, i-1):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]
