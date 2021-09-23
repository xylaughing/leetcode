class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict_minAmount = {}
        
        # for node i, the cost is max(cost of left, cost of right) + i
        def Cost(l, r):
            if (l, r) in dict_minAmount: 
                return dict_minAmount[(l, r)]
            if r <= l:
                return 0
            else:
                minAmount = float('inf')
                for i in range(l, r):
                    minAmount = min(minAmount, max(Cost(l, i-1), Cost(i+1, r)) + i)
            dict_minAmount[(l, r)] = minAmount 
            return minAmount
            
        result = Cost(1, n)      
        return result
