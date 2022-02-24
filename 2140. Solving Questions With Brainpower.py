class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
    
        dp = [[0, 0] for _ in range(n)]
        dp[n-1] = [questions[n-1][0], 0]

        for i in range(n-2, -1, -1):
            if i + 1 + questions[i][1] < n:
                dp[i][0] = questions[i][0] + max(dp[i + 1 + questions[i][1]])
            else:
                dp[i][0] = questions[i][0]
            dp[i][1] =  max(dp[i+1])
        return max(dp[0])
