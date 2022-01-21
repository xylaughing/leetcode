class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        cool[i] = max(cool[i - 1], sell[i - 1]); // Stay at cooldown, or rest from sell
        buy[i] = max(buy[i - 1], cool[i - 1] - prices[i]); // Stay at buy, or buy from cooldown
        sell[i] = buy[i - 1] + prices[i];  // Only one way from buy
        """
        
        cool, buy, sell = 0, -prices[0], 0
        for i in range(1, len(prices)):
            prevsell = sell
            sell = buy + prices[i]
            buy = max(buy, cool - prices[i])
            cool = max(cool, prevsell)
        return max(cool, sell)
