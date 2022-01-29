class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        def helper(exp):
            if exp.isnumeric():
                return [int(exp)]
            res = []
            for i in range(len(exp)):
                if not exp[i].isnumeric():
                    leftvals = helper(exp[0:i])
                    rightvals = helper(exp[i+1:])
                    for leftval in leftvals:
                        for rightval in rightvals:
                            res.append(eval(str(leftval) + exp[i] + str(rightval)))
            return res
        
        return helper(expression)
