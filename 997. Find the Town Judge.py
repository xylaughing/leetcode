class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1: return 1
        if not trust: return -1
        dp = {}
        people = zip(*trust)[0]
        for i, j in trust:
            if j not in dp:
                dp[j] = [i]
            else:
                dp[j].append(i)            
        for x in dp:
            if len(dp[x]) == n-1 and x not in people:
                return x
        return -1
        
        """ 
        count = [0] * (n + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        print(count)
        for i in range(1, n + 1):
            if count[i] == n - 1:
                return i
        return -1
        """
