class Solution(object):    
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        """
        def dfs(s1, s2, s3, p1, p2):
            if p1+p2 == len(s3): return True
            if len(s1) == p1: return True if s2[p2:] == s3[p1+p2:] else False
            if len(s2) == p2: return True if s1[p1:] == s3[p1+p2:] else False
            #print(p1, p2, s1[p1], s2[p2], s3[p1+p2])
            res = False
            if s3[p1+p2] == s1[p1]:
                res |= dfs(s1, s2, s3, p1+1, p2)
            if s3[p1+p2] == s2[p2]:
                res |= dfs(s1, s2, s3, p1, p2+1)
            return res
        
        if len(s1) + len(s2) != len(s3): return False
        return dfs(s1, s2, s3, 0, 0)
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[m][n] = True
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i+j]:
                    dp[i][j] |= dp[i+1][j]
                if j < n and s2[j] == s3[i+j]:
                    dp[i][j] |= dp[i][j+1]
        return dp[0][0]
        
