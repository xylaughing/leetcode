class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """    
        if n == 1: return ["()"]
        prev = self.generateParenthesis(n-1)
        res = []
        for x in prev:
            res.append("()" + x)
            i = 0
            while x[i] == "(":
                res.append(x[0:i+1] + "()" + x[i+1:])
                i += 1
        return res
                
