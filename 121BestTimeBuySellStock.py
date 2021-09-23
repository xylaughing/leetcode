class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def maxSubArr(profits):
            # type profits: List[int]
            local_max = 0
            global_max = float ('-inf')
            for i in range(len(profits)):
                local_max = max( profits[i], profits[i] + local_max)
                if local_max > global_max:
                    global_max = local_max
            return global_max
        
        newlist = []
        for i in range(len(prices)-1):
            newlist.append(prices[i+1] - prices[i])  
        
        max_profit = maxSubArr(newlist)
        
        if max_profit < 0:
            return 0
        else:
            return max_profit
